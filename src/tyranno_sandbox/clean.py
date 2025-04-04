# SPDX-FileCopyrightText: Copyright 2020-2025, Contributors to Tyrannosaurus
# SPDX-PackageHomePage: https://github.com/dmyersturnbull/tyrannosaurus
# SPDX-License-Identifier: Apache-2.0
"""
`tyranno clean` command.
"""

import shutil
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

from tyranno_sandbox.context import Context

__all__ = ["Cleaner"]


@dataclass(frozen=True, slots=True)
class Cleaner:
    """"""

    context: Context

    def run(self) -> Iterator[Path]:
        for path in self.context.find_trash():
            self._trash(path)
            yield path

    def _trash(self, source: Path) -> None:
        dest = self.context.trash_dir / source
        if not self.context.dry_run:
            dest.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(str(source), str(dest))
