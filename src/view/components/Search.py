from textual.widgets import Static, Input, Button
from textual.containers import Horizontal

from core.typedef import vec_T_str

class FSearchConfig():
        HEADER          = Static("")
        SEARCH_ICON     = ''
        HINT            = "Search Directory Here"
        HINT_ICON       = ''

        def __init__(self, config: dict) -> None:
                self.HEADER             = config["header"]
                self.SEARCH_ICON        = config["s_icon"]
                self.HINT               = config["hint"]
                self.HINT_ICON          = config["h_icon"]

class FSearchWidget(Static):
        
        CSS_PATH        = "compress-scr.css"
        CONFIG          = None

        # Optional
        HEADER          = ""

        LAYOUT          = Static("FSearchWidget.LAYOUT err")

        def __init__(self, config=None):
                super().__init__()
                self.CONFIG     = config
                self.__build_component()
        
        def __build_component(self):
                if self.CONFIG != None:
                        self.LAYOUT = Horizontal(
                                Input(placeholder="[] Directory Location:", id="Search-field"),
                                Button("[] Search", id="Search-button"),

                                id="Search-widget"
                        )

        def compose(self):
                yield self.LAYOUT
