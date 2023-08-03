import os
from pathlib import Path

INPUT_DIR = [("No Files Selected", 0)]

STATISTICS = [
        ("Files Processed:", "0"),
        ("Total Source Size:", "0"),
        ("Total Export Size:", "0"),
        ("Size Reduced:", "0"),
        ("Size Compression Rate:", "0"),
]

TEST_FILE_ENTRIES = [
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_1", "120GB"),
        ("Video_test_test_X", "120GB"),
        ("Video_test_test_X", "120GB"),

]

TEST_PATHS_STR = [
        "~/dev/Python/Vult/tests/demo_video1.mp4",
        "~/dev/Python/Vult/tests/demo_video2.mp4",
        "~/dev/Python/Vult/tests/demo_video3.mp4",
]

TEST_PATHS = [
        Path("~/dev/Python/Vult/tests/demo_video1.mp4"),
        Path("~/dev/Python/Vult/tests/demo_video2.mp4"),
        Path("~/dev/Python/Vult/tests/demo_video3.mp4"),
]

TEST_SIZES = [
        0, 15,20, 15402323, 523, 12
]

TEST_SIZES_STR = [
        "0", "15", "20", "15402323", "523", "12"
]

def log(logfile: str, entry):
        LOGFILE = 0
        if not os.path.isfile(logfile):
                open(logfile, "x")

        LOGFILE     = open(logfile, "at")

        LOGFILE.write(str(entry) + '\n')
        LOGFILE.close()
