import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from vult.core.vult_core import Core
from vult.util.dev_utils import log

if __name__ == '__main__':
        log('log', '===== Init [test_core] =====')
        print(f'Working Directory: {os.getcwd()}')
        test_src_dir    = "./tests/res"
        # test_src_dir    = "./tests/res"

        # Prefix
        if test_src_dir[0 : 2] == './':
                print("current dir")
        elif test_src_dir[0 : 3] == '../':
                print("parent dir")

        splr = test_src_dir
        sources         = Core.build_sources(test_src_dir)