from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

import pytest

from PIL import Image, ImageShow

from .helper import hopper, is_win32, on_ci


def test_windows_viewer_rejects_quotes_and_escapes_percent_expansion() -> None:
    viewer = ImageShow.WindowsViewer()
    with pytest.raises(ValueError, match="double quotes"):
        viewer.get_command('invalid"name.png')
    command = viewer.get_command("%PILLOW_TEST%.png")
    assert '"%"PILLOW_TEST"%".png' in command


def test_windows_viewer_passes_literal_filename_to_os(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    path = tmp_path / "%PILLOW_TEST% & (image).png"
    path.write_bytes(b"image")
    launched = []
    cleanup = []
    monkeypatch.setattr(sys, "platform", "win32")
    monkeypatch.setattr(os, "startfile", launched.append, raising=False)
    monkeypatch.setattr(ImageShow.subprocess, "Popen", cleanup.append)
    assert ImageShow.WindowsViewer().show_file(str(path)) == 1
    assert launched == [str(path)]
    assert cleanup
    assert cleanup[0][-1] == str(path)


def test_sanity() -> None:
    dir(Image)
    dir(ImageShow)


def test_register() -> None:
    # Test registering a viewer that is an instance
    class TestViewer(ImageShow.Viewer):
        pass

    ImageShow.register(TestViewer())

    # Restore original state
    ImageShow._viewers.pop()


@pytest.mark.parametrize(
    "order",
    [-1, 0],
)
def test_viewer_show(order: int) -> None:
    class TestViewer(ImageShow.Viewer):
        def show_image(self, image: Image.Image, **options: Any) -> bool:
            self.methodCalled = True
            return True

    viewer = TestViewer()
    ImageShow.register(viewer, order)

    for mode in ("1", "I;16", "LA", "RGB", "RGBA"):
        viewer.methodCalled = False
        with hopper(mode) as im:
            assert ImageShow.show(im)
        assert viewer.methodCalled

    # Restore original state
    ImageShow._viewers.pop(0)


@pytest.mark.skipif(
    not on_ci() or is_win32(),
    reason="Only run on CIs; hangs on Windows CIs",
)
@pytest.mark.parametrize("mode", ("1", "I;16", "LA", "RGB", "RGBA"))
def test_show(mode: str) -> None:
    im = hopper(mode)
    assert ImageShow.show(im)


def test_show_without_viewers() -> None:
    viewers = ImageShow._viewers
    ImageShow._viewers = []

    with hopper() as im:
        assert not ImageShow.show(im)

    ImageShow._viewers = viewers


@pytest.mark.parametrize(
    "viewer",
    (
        ImageShow.Viewer(),
        ImageShow.WindowsViewer(),
        ImageShow.MacViewer(),
        ImageShow.XDGViewer(),
        ImageShow.DisplayViewer(),
        ImageShow.GmDisplayViewer(),
        ImageShow.EogViewer(),
        ImageShow.XVViewer(),
        ImageShow.IPythonViewer(),
    ),
)
def test_show_file(viewer: ImageShow.Viewer) -> None:
    assert not os.path.exists("missing.png")

    with pytest.raises(FileNotFoundError):
        viewer.show_file("missing.png")


def test_viewer() -> None:
    viewer = ImageShow.Viewer()

    im = Image.new("L", (1, 1))
    assert viewer.get_format(im) is None

    with pytest.raises(NotImplementedError):
        viewer.get_command("")


@pytest.mark.parametrize("viewer", ImageShow._viewers)
def test_viewers(viewer: ImageShow.Viewer) -> None:
    try:
        viewer.get_command("test.jpg")
    except NotImplementedError:
        pass


def test_ipythonviewer() -> None:
    pytest.importorskip("IPython", reason="IPython not installed")
    for viewer in ImageShow._viewers:
        if isinstance(viewer, ImageShow.IPythonViewer):
            test_viewer = viewer
            break
    else:
        pytest.fail("IPythonViewer not found")

    with hopper() as im:
        assert test_viewer.show(im) == 1
