<p align="center">
    <img width="248" height="250" src="https://raw.githubusercontent.com/python-pillow/pillow-logo/main/pillow-logo-248x250.png" alt="Pillow logo">
</p>

# Pillow

## Python Imaging Library (Fork)

Pillow is the friendly PIL fork by [Jeffrey A. Clark and
contributors](https://github.com/python-pillow/Pillow/graphs/contributors).
PIL is the Python Imaging Library by Fredrik Lundh and contributors.
As of 2019, Pillow development is
[supported by Tidelift](https://tidelift.com/subscription/pkg/pypi-pillow?utm_source=pypi-pillow&utm_medium=readme&utm_campaign=enterprise).

<table>
    <tr>
        <th>docs</th>
        <td>
            <a href="https://pillow.readthedocs.io/?badge=latest"><img
                alt="Documentation Status"
                src="https://readthedocs.org/projects/pillow/badge/?version=latest"></a>
        </td>
    </tr>
    <tr>
        <th>tests</th>
        <td>
            <a href="https://github.com/python-pillow/Pillow/actions/workflows/lint.yml"><img
                alt="GitHub Actions build status (Lint)"
                src="https://github.com/python-pillow/Pillow/workflows/Lint/badge.svg"></a>
            <a href="https://github.com/python-pillow/Pillow/actions/workflows/test.yml"><img
                alt="GitHub Actions build status (Test Linux and macOS)"
                src="https://github.com/python-pillow/Pillow/workflows/Test/badge.svg"></a>
            <a href="https://github.com/python-pillow/Pillow/actions/workflows/test-windows.yml"><img
                alt="GitHub Actions build status (Test Windows)"
                src="https://github.com/python-pillow/Pillow/workflows/Test%20Windows/badge.svg"></a>
            <a href="https://github.com/python-pillow/Pillow/actions/workflows/test-mingw.yml"><img
                alt="GitHub Actions build status (Test MinGW)"
                src="https://github.com/python-pillow/Pillow/workflows/Test%20MinGW/badge.svg"></a>
            <a href="https://github.com/python-pillow/Pillow/actions/workflows/test-cygwin.yml"><img
                alt="GitHub Actions build status (Test Cygwin)"
                src="https://github.com/python-pillow/Pillow/workflows/Test%20Cygwin/badge.svg"></a>
            <a href="https://github.com/python-pillow/Pillow/actions/workflows/test-docker.yml"><img
                alt="GitHub Actions build status (Test Docker)"
                src="https://github.com/python-pillow/Pillow/workflows/Test%20Docker/badge.svg"></a>
            <a href="https://github.com/python-pillow/Pillow/actions/workflows/wheels.yml"><img
                alt="GitHub Actions build status (Wheels)"
                src="https://github.com/python-pillow/Pillow/workflows/Wheels/badge.svg"></a>
            <a href="https://app.codecov.io/gh/python-pillow/Pillow"><img
                alt="Code coverage"
                src="https://codecov.io/gh/python-pillow/Pillow/branch/main/graph/badge.svg"></a>
            <a href="https://issues.oss-fuzz.com/issues?q=title:pillow"><img
                alt="Fuzzing Status"
                src="https://oss-fuzz-build-logs.storage.googleapis.com/badges/pillow.svg"></a>
        </td>
    </tr>
    <tr>
        <th>package</th>
        <td>
            <a href="https://zenodo.org/badge/latestdoi/17549/python-pillow/Pillow"><img
                alt="Zenodo"
                src="https://zenodo.org/badge/17549/python-pillow/Pillow.svg"></a>
            <a href="https://tidelift.com/subscription/pkg/pypi-pillow?utm_source=pypi-pillow&utm_medium=badge"><img
                alt="Tidelift"
                src="https://tidelift.com/badges/package/pypi/pillow?style=flat"></a>
            <a href="https://pypi.org/project/pillow/"><img
                alt="Newest PyPI version"
                src="https://img.shields.io/pypi/v/pillow.svg"></a>
            <a href="https://pypi.org/project/pillow/"><img
                alt="Number of PyPI downloads"
                src="https://img.shields.io/pypi/dm/pillow.svg"></a>
            <a href="https://www.bestpractices.dev/projects/6331"><img
                alt="OpenSSF Best Practices"
                src="https://www.bestpractices.dev/projects/6331/badge"></a>
        </td>
    </tr>
    <tr>
        <th>social</th>
        <td>
            <a href="https://gitter.im/python-pillow/Pillow?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge"><img
                alt="Join the chat at https://gitter.im/python-pillow/Pillow"
                src="https://badges.gitter.im/python-pillow/Pillow.svg"></a>
            <a href="https://fosstodon.org/@pillow"><img
                alt="Follow on https://fosstodon.org/@pillow"
                src="https://img.shields.io/badge/publish-on%20Mastodon-595aff.svg"
                rel="me"></a>
        </td>
    </tr>
</table>

## Overview

The Python Imaging Library adds image processing capabilities to your Python interpreter.

This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

The core image library is designed for fast access to data stored in a few basic pixel formats. It should provide a solid foundation for a general image processing tool.

## More information

This fork preserves Pillow 11.3 APIs and backports security fixes from upstream
python-pillow/Pillow. Its version identifies the maintained backport separately
from upstream releases. Native codecs remain enabled.

Patch provenance: a9ffc42bedf4fc0a7ef8d6486e7f9e81e3397721,
13ada41172142f2fd9f0906f615a00ea623a11ca,
f7a31ea75e460e108c37126da1f47812f21f6b09,
ceefc348eb3c3844c7f9796ef2cc3a7dd5fbba7b,
eada3cbd7fb9963ee90673fb7b5270124a0d5f4b,
cce3bdb867c77a3420261ed1bfdb6b0787ec8fc1,
b0e06caa64c1405aa3da0bb1d2bd9a77ca22de7f,
88194166691b7b603529b8b036ab3ab9cedd2de4,
8404ea5fe5df40fc34aa1e51403dd6fce0778b8a,
f39b0ae6624eb2d7c5c5d651d9bb5fdbd96a8675,
0a263e6264aa5399988d9acd3bbfbca2ca3ec77d,
6a8de891fb00968e5ea79bfa84368ed90b3cfc1d,
58f9a1d166dcb0c274807d4423522d205b0c35ea,
3bf614e4b8615d0ce1d5039efaf6db447fe7c468,
ec8272044d2adfc97a5f4b6e921c1a908318d9cb,
cf6de8ca9b23e714aa5310e1c791eda66fc0b670,
3cb854e8b2bab43f40e342e665f9340d861aa628,
54ba4db542ad3c7b918812a4e2d69c27735a3199,
78ee80a6fdd4b787f71880f10e66d6b989c6e58d,
f0f67f8cf86e6fc049dec23996c41653a5fdd63f, and
64f6d4ebd878d00b581812faab3f9863576470e6.

Adaptations retain the 11.3 default tile extent convention and two-margin
filter API, check both PCF metric formats, validate mapped row sizes and offsets,
and use widened arithmetic before allocation or subtraction. The filter checks
also avoid zero division and signed overflow in the newer upstream guard.
Empty images reject border expansion while zero-margin copies remain valid.
Long-text advance accumulation uses 64-bit arithmetic alongside the upstream
glyph-position fix.

- [Documentation](https://pillow.readthedocs.io/)
  - [Installation](https://pillow.readthedocs.io/en/latest/installation/basic-installation.html)
  - [Handbook](https://pillow.readthedocs.io/en/latest/handbook/index.html)
- [Contribute](https://github.com/python-pillow/Pillow/blob/main/.github/CONTRIBUTING.md)
  - [Issues](https://github.com/python-pillow/Pillow/issues)
  - [Pull requests](https://github.com/python-pillow/Pillow/pulls)
- [Release notes](https://pillow.readthedocs.io/en/stable/releasenotes/index.html)
- [Changelog](https://github.com/python-pillow/Pillow/releases)
  - [Pre-fork](https://github.com/python-pillow/Pillow/blob/main/CHANGES.rst#pre-fork)

## Report a vulnerability

To report a security vulnerability, please follow the procedure described in the [Tidelift security policy](https://tidelift.com/docs/security).
