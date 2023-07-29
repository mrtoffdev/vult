from __future__ import annotations

import os
from pathlib import Path
from util.dev_utils import log

class Core:
        @staticmethod
        def validate_file(source_dir: str | Path, file: str | Path) -> bool:
                log("fs", "bs file found & validating: " + str(file))
                # Vult Supported Formats
                SUPPORTED_FORMATS = [
                    ".mp4",
                    ".mkv",
                    ".mov",
                    ".avi"
                ]

                log("fs", "bs file check: " + str(os.path.isfile(str(source_dir) +
                                                                 str(file))))
                log("fs", "bs split result: " + str(os.path.splitext(file)))

                # Validate
                if  os.path.isfile(str(source_dir) + str(file)) and \
                    os.path.splitext(file)[1] in SUPPORTED_FORMATS:
                        return True
                else:
                        return False

        @staticmethod
        def build_sources(source_dir: str | Path) -> [(str, str)]:
                log("fs", "bs path rcv: " + source_dir)

                paths = [
                        file for file in os.listdir(Path(source_dir)) if
                        Core.validate_file(source_dir, file)
                ]
                log("fs", "paths: " + str(paths))
                sizes = []

                log("logfile.txt", "From rebuild_sources: paths=" + str(paths))

                for path in paths:
                    sizes.append(str(os.path.getsize(str(source_dir) + path)))

                return list(zip(paths, sizes))



