from __future__ import annotations

import os
from pathlib import Path
from util.dev_utils import log

class Core:
        @staticmethod
        def validate_file(file: str | Path) -> bool:
                # Vult Supported Formats
                SUPPORTED_FORMATS = [
                    ".mp4",
                    ".mkv",
                    ".mov",
                    ".avi"
                ]

                # Validate
                if  os.path.isfile(file) and \
                    os.path.splitext(file)[1] in SUPPORTED_FORMATS:
                        return True
                else:
                        return False

        @staticmethod
        def build_sources(source_dir: str | Path) -> [(str, str)]:
                paths = [
                        file for file in os.listdir(source_dir)
                        if Core.validate_file(file)
                ]
                sizes = []

                log("logfile.txt", "From rebuild_sources: paths=" + str(paths))

                for path in paths:
                    sizes.append(str(os.path.getsize(path)))

                return list(zip(paths, sizes))



