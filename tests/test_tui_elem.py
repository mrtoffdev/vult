import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from textual.app import App, ComposeResult

CSS_PATH = "../vult/compress-scr.css"


# InputForm ----------
from vult.view.components.InputForm import InputForm
def test_InputForm():

        class InputFormTest(App[str]):
                def compose(self) -> ComposeResult:
                        yield InputForm()

        print("InputForm")
        app = InputFormTest(css_path=CSS_PATH)
        print(app.run())



# Table --------------
from vult.view.components.Table import Table, TableHeader, TableEntry
def test_Table():

        class TableTest(App[str]):
                config = [
                        ["TableTest: ", "TableTest1:"],
                        [
                                ["TTest Entry 1", "100"],
                                ["TTest Entry 2", "100"],
                                ["TTest Entry 3", "100"],
                                ["TTest Entry 4", "100"],
                                ["TTest Entry 5", "100"],
                        ]
                ]

                def compose(self) -> ComposeResult:
                        # yield Static("Test Test")
                        yield Table(id="TableOne",
                                    config=self.config)

        class TableHeaderTest(App[str]):
                def compose(self) -> ComposeResult:
                        yield TableHeader(["Test Header: ", "Test Header 2: "])

        class TableEntryTest(App[str]):
                def compose(self) -> ComposeResult:
                        yield TableEntry(["Test Entry", "Test Entry 1"])

        app = TableTest(css_path=CSS_PATH)
        # app = TableHeaderTest(css_path=CSS_PATH)
        # app = TableEntryTest(css_path=CSS_PATH)

        print(app.run())

from vult.view.components.Explorer import Explorer
def test_Explorer():
        class ExplorerTest(App[str]):
                def compose(self) -> ComposeResult:
                        yield Explorer()

        app = ExplorerTest(css_path=CSS_PATH)
        print(app.run())

if __name__ == '__main__':
        test_Explorer()
        # test_Table()
