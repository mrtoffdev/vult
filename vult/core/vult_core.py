from __future__ import annotations

import os
from pathlib import Path

"""
        Entry Collection
        File names serve as the index of every entry in the collection. IDs are
        generated though Short Unique ID generation, prefixed with the widget ID,
        which serve as global DOM & backend identifiers. This does not apply to
        TUI elements as there is little to no need for dynamically assigned IDs
        since most widgets are static. As such, their IDs are hardcoded during
        development
        
        [
                "{File Name}": ("{ID}", "{Size}"),
                "{File Name}": ("{ID}", "{Size}"),
                "{File Name}": ("{ID}", "{Size}"),
                ...
        ]
"""

class Core:
        @staticmethod
        def validate_file(source_dir: str | Path, file: str | Path) -> bool:
                # log("fs", "bs file found & validating: " + str(file))

                # Vult Supported Formats
                SUPPORTED_FORMATS = [
                    ".mp4",
                    ".mkv",
                    ".mov",
                    ".avi"
                ]

                # log("fs", "bs file check: " + str(os.path.isfile(str(source_dir) +
                # log("fs", "bs split result: " + str(os.path.splitext(file)))

                # Validate
                return (os.path.isfile(str(source_dir) + str(file)) and
                        os.path.splitext(file)[1] in SUPPORTED_FORMATS)

        @staticmethod
        def build_sources(source_dir: str | Path) -> [(str, str)]:
                # log("fs", "bs path rcv: " + source_dir)

                paths = sorted([
                        file for file in os.listdir(Path(source_dir)) if
                        Core.validate_file(source_dir, file)
                ])

                sizes = [
                        os.path.getsize(str(source_dir) + path) for path in paths
                ]

                # log("fs", "paths: " + str(paths))
                # log("logfile.txt", "From rebuild_sources: paths=" + str(paths))

                return list(zip(paths, sizes))



