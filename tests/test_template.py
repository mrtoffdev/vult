# ---------- Path ----------
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
# --------------------------


# ---------- Global --------
from vult.util.dev_utils import log
import pytest
# --------------------------


# Example Test 1
# ----- Test Imports -------
from vult.core.vult_core import Core
# ------ Definition --------
def test_testname():
        # Insert test details
        pass
# --------------------------


# Example Test 2
# ----- Test Imports -------
from vult.view.components.Explorer import Explorer, ExplorerLayout
# ------ Definition --------
def test_testname2():
        # Insert test details
        pass
# --------------------------



# ---------- Main ----------
if __name__ == '__main__':
        # Insert pre-testing environment / conditions
        log('log', '===== Init [test_template] =====')