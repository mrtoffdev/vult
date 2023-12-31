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
        def validate_file(file: str | Path) -> bool:
                log("fs", "Received file to be validated: " + str(file))

                # Vult Supported Formats
                SUPPORTED_FORMATS = [
                    ".mp4",
                    ".mkv",
                    ".mov",
                    ".avi"
                ]

                STATUS: bool    = False
                IS_FILE: bool   = os.path.isfile(file)
                EXTENSION: str  = os.path.splitext(file)[1]

                # Placeholder for possible extension
                if IS_FILE and EXTENSION in SUPPORTED_FORMATS:
                        STATUS = True
                else:
                        STATUS = False

                # Validate
                log('fs', f'validate_file(): status: {str(STATUS)}')
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
                        DIR_PATH = os.path.join(os.getcwd(), dir)

                return DIR_PATH

        @staticmethod
        def build_sources(source_dir: str | Path) -> [(str, str)]:
                log('log', f'build_sources(): received {str(source_dir)}')

                # Build absolute path from input src_dir
                src_path = Core.build_path(source_dir)
                log('log', f'build_sources(): received {str(src_path)}')

                # Generating absolute paths from filenames
                paths = sorted([
                        os.path.join(src_path, file) for file \
                        in os.listdir(Path(src_path)) \
                        if Core.validate_file(os.path.join(src_path, file))
                ])
                log('log', f'Built Files: {str(paths)}')

                # Split filenames from paths
                file_names = [
                        name.split('/')[len(name.split('/')) - 1] for name in paths
                ]
                log('log', f'build_sources() > filenames: {str(file_names)}')

                '''
                        ==== Transcoding resolution =====
                        Input Formats: mp4, avi, mkv
                        
                        Output Format: mp4
                        Codec: h265, avi (beta)
                        
                '''

                # Generate FFMPEG models from paths
                files = ([
                        ffmpeg.input(file) for file  in paths
                ])

                # Parse file sizes
                sizes = [
                        os.path.getsize(str(path)) for path in paths
                ]
                log('fs', f'build_sources() > sizes: {str(sizes)}')

                # Test file codec detail fetching
                for path in paths:
                        try:
                                log('log',f'Codec info:')
                                log('log', f'{ffmpeg.probe(path)}', mode='json')
                        except ffmpeg._run.Error:
                                log('log', f'build_sources() > ffmpeg probe: Invalid '
                                           f'File {path}')

                # log("fs", "paths: " + str(paths))
                # log("logfile.txt", "From rebuild_sources: paths=" + str(paths))

                def validate_codec(entry) -> bool:
                        try:
                                probe_result = ffmpeg.probe(entry)
                                return probe_result != "" or probe_result is not None

                        except ffmpeg._run.Error:
                                return False




                VALIDATED_PATH = [
                        entry for entry in paths if validate_codec(entry)
                ]

                for path in VALIDATED_PATH:
                        log('log', f'{str(path)}')

                '''
                FFMPEG CLI Options:
                -fpsmax
                -vcodec
                -aspect (Container Level, not Frame Level)
                -pass (1pass / 2pass encoding)
                -pixfmt
                -cuda (for nvidia hardware)
                -opencl (for OpenCL acceleration)
                -init_hw_device [name]
                -init_hw_device list
                -hwaccel [ use w/ driver (vdpau, dxva2, vaapi, d3d11va)
                -preset [val]
                -c:v (codec)
                -crf [val]
                '''

                return list(zip(paths, sizes))



