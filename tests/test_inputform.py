import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from textual.app import App, ComposeResult
from vult.view.components.InputForm import InputForm

# InputForm -----
class InputFormTest(App[str]):
        def compose(self) -> ComposeResult:
                yield InputForm()

# Table ---------
from vult.view.components.Table import Table
class TableTest(App[str]):
        def compose(self) -> ComposeResult:
                yield Table()

if __name__ == '__main__':
        # app = InputFormTest(css_path="../vult/compress-scr.css")
        app = TableTest(css_path="../vult/compress-scr.css")
        print(app.run())