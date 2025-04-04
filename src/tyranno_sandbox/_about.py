# SPDX-FileCopyrightText: Copyright 2020-2025, Contributors to Tyrannosaurus
# SPDX-PackageHomePage: https://github.com/dmyersturnbull/tyrannosaurus
# SPDX-License-Identifier: Apache-2.0

"""
Tyrannosaurus project metadata.

This is a separate module so that it's easy to import.
For example, your `mypkg/app.py` may want to write `"{__about__.name} (version v{__about__.version})"`,
while your `mypkg/__init__.py` includes lines like `from mypkg.app import Entry` for its public API.
(This would break if `mypkg.app` tried to `from mypkg import __about__`.)
"""

import time
from collections.abc import Sequence
from datetime import UTC, datetime
from typing import NotRequired, ReadOnly, TypedDict, overload

__all__ = ["About", "UrlDict", "__about__", "start_time_monotonic"]
start_time_monotonic = time.monotonic()
start_time_utc = datetime.now().astimezone(UTC)


class _FrozenList[T](Sequence[T]):
    def __init__(self, *items: T) -> None:
        self.__items = list(items)

    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...

    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        return self.__items[index]

    def __len__(self):
        return len(self.__items)

    def __hash__(self) -> int:
        return hash(tuple(self.__items))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, _FrozenList):
            return self.__items == other.__items
        if isinstance(other, Sequence):
            return self.__items == list(other)
        return NotImplemented


class UrlDict(TypedDict):
    """
    URLs for this project, [per PyPi](https://docs.pypi.org/project_metadata/).
    Names are from the `name` column, lowercased.
    `homepage`, `changelog`, and `source` are required.
    """

    homepage: ReadOnly[str]
    changelog: ReadOnly[str]
    source: ReadOnly[str]
    documentation: NotRequired[ReadOnly[str]]
    download: NotRequired[ReadOnly[str]]
    bug: NotRequired[ReadOnly[str]]
    funding: NotRequired[ReadOnly[str]]


class About(TypedDict):
    """
    Metadata about this package.

    Attributes:
        namespace: name of the directory containing this module.
        name: pyproject `project.name`                   / importlib `Name`    .
        version: pyproject `project.version`             / importlib `version`.
        summary: pyproject `project.description`         / importlib `Summary`.
        license: pyproject `project.license.text`        / importlib `License`;
          an SPDX ID such as `Apache-2.0`.
        authors: pyproject `project.authors[*].name`     / importlib `Author` split by ` and `;
          e.g. `["Kerri Kerrigan", "Adam Addison"]`.
        maintainers: pyproject `project.authors[*].name` / importlib `Author` split by ` and `;
          e.g. `["Kerri Kerrigan", "Adam Addison"]`.
        keywords: pyproject `project.keywords`           / importlib `Keywords`.
        urls: pyproject  `project.urls` subset           / `Project-URL` subset.
          Only recognized general URLs from
          [PyPi Project Metadata](https://docs.pypi.org/project_metadata/).
          Attributes are lowercased versions of the "Name", from the "General URL" table.
    """

    name: ReadOnly[str]
    namespace: ReadOnly[str]
    version: ReadOnly[str]
    summary: ReadOnly[str]
    license: ReadOnly[str]
    authors: ReadOnly[Sequence[str]]
    maintainers: ReadOnly[Sequence[str]]
    keywords: ReadOnly[Sequence[str]]
    urls: ReadOnly[UrlDict]


__about__ = About(
    # :tyranno: name="${{.namespace}}",
    namespace="tyranno_sandbox",
    # :tyranno: name="${{project.name}}",
    name="tyranno-sandbox",
    # :tyranno: version="${{project.version}}",
    version="0.0.1-alpha0",
    # :tyranno: summary="${{project.summary}}",
    summary="Sandbox to test CI/CD in Tyrannosaurus",
    # :tyranno: authors=${{project.authors[*].name}},
    authors=["Douglas Myers-Turnbull"],
    # :tyranno: maintainers=${{project.maintainers[*].name}},
    maintainers=["Douglas Myers-Turnbull"],
    # :tyranno: name=${{project.keywords}},
    keywords=["ci/cd", "cookiecutter", "github-workflow", "pyproject", "python-template"],
    # :tyranno: license="${{project.license.text}}",
    license="Apache-2.0",
    urls=UrlDict(
        # :tyranno: homepage="${{project.urls.Homepage}}",
        homepage="https://github.com/dmyersturnbull/tyranno-sandbox",
        # :tyranno: source="${{project.urls.Source}}",
        source="https://github.com/dmyersturnbull/tyranno-sandbox",
        # :tyranno: documentation="${{project.urls.Documentation}}",
        documentation="https://github.com/dmyersturnbull/tyranno-sandbox",
        # :tyranno: changelog="${{project.urls.Release Notes}}",
        changelog="https://github.com/dmyersturnbull/tyranno-sandbox/releases",
        # :tyranno: download="${{project.urls.Download}}",
        download="https://pypi.org/project/tyranno-sandbox/",
        # :tyranno: bug="${{project.urls.Tracker}}",
        bug="https://github.com/dmyersturnbull/tyranno-sandbox/issues",
    ),
)
