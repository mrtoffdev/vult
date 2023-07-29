import os

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

def log(logfile: str, entry):
        LOGFILE = 0
        if os.path.isfile(logfile):
                LOGFILE     = open(logfile, "at")
        else:
                open(logfile, "x")
                LOGFILE     = open(logfile, "at")

        LOGFILE.write(str(entry) + '\n')
        LOGFILE.close()
