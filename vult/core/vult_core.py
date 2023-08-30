from __future__ import annotations

import os
from pathlib import Path


from vult.util.dev_utils import log

import ffmpeg


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
                log("fs", "bs file found & validating: " + str(file))

                # Vult Supported Formats
                SUPPORTED_FORMATS = [
                    ".mp4",
                    ".mkv",
                    ".mov",
                    ".avi"
                ]

                # log("fs", "bs file check: " + str(os.path.isfile(str(source_dir) +
                # log("fs", "bs split result: " + str(os.path.splitext(file)))
                if (os.path.isfile(str(source_dir) + str(file)) and
                        os.path.splitext(file)[1] in SUPPORTED_FORMATS):
                        log('log', 'File is valid')
                else:
                        log('log', 'File is invalid')

                # Validate
                return STATUS

        @staticmethod
        def build_path(dir: str | Path):

                DIR_PATH: str
                PREFIX_SLICE = dir[0:3]

                if PREFIX_SLICE[0] == '/':
                        DIR_PATH = dir
                elif PREFIX_SLICE[0:2] == './':
                        DIR_PATH = os.path.join(os.getcwd(), dir.lstrip('./'))
                elif PREFIX_SLICE[0:3] == '../':
                        DIR_PATH = os.path.join(os.getcwd(), '..', dir.lstrip('../'))
                else:
                        DIR_PATH = 'invalid'

                return DIR_PATH

        @staticmethod
        def build_sources(source_dir: str | Path) -> [(str, str)]:
                src_path = Core.build_path(source_dir)

                paths = sorted([
                        file for file in os.listdir(Path(source_dir_extended)) if
                        Core.validate_file(source_dir_extended, file)
                ])
                '''
                        ==== Transcoding resolution =====
                        Input Formats: mp4, avi, mkv
                        
                        Output Format: mp4
                        Codec: h265, avi (beta)
                        
                '''
                log('log', f'Received Src Dir: {source_dir}')
                log('log', f'Built Files: {str(paths)}')

                # Fetch valid files from source dir
                files = ([
                        ffmpeg.input(file) for file  in paths
                ])


                # Generate FFMPEG models from paths
                sizes = [
                        os.path.getsize(str(source_dir) + path) for path in paths
                ]

                # Test file codec detail fetching
                for path in paths:
                        log('log',f'Codec info: {ffmpeg.probe(path)}')

                # log("fs", "paths: " + str(paths))
                # log("logfile.txt", "From rebuild_sources: paths=" + str(paths))

                return list(zip(paths, sizes))



