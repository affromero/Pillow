from __future__ import annotations

from importlib.metadata import metadata

import pytest

pyroma = pytest.importorskip("pyroma", reason="Pyroma not installed")


def test_pyroma() -> None:
    # Arrange
    package_metadata = metadata("Pillow")
    data = {}
    for key in set(package_metadata.keys()):
        values = package_metadata.get_all(key)
        data[pyroma.projectdata.normalize(key)] = (
            values[0] if len(values) == 1 else values
        )
    data["description"] = package_metadata.get_payload().strip()

    # Act
    rating = pyroma.ratings.rate(data)

    # Assert
    assert rating == (10, [])
