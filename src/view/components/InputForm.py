from textual.widgets import Static, Input, Button
from textual.containers import Horizontal

from core.typedef import vec_T_str

class IInputForm:
        # Default Configuration
        HEADER          = Static("")
        SEARCH_ICON     = ''
        HINT            = "Search Directory Here"
        HINT_ICON       = ''

        # State
        SEARCH_VALUE    = ""

        # DOM
        ID              = None
        CSS_PATH        = None

        def __init__(self, config: dict) -> None:
                self.HEADER             = config["header"]
                self.SEARCH_ICON        = config["s_icon"]
                self.HINT               = config["hint"]
                self.HINT_ICON          = config["h_icon"]

class InputForm(Static):
        
        CSS_PATH        = None
        CONFIG          = IInputForm({
                "header": "[] Directory Location:",
                "s_icon": '',
                "hint"  : "[] Directory Location:",
                "h_icon": ''
        })

        # Optional
        HEADER          = ""
        HINT            = ""

        LAYOUT          = Static("FSearchWidget.LAYOUT err")

        def __init__(self, config=None, id=None):
                super().__init__(id=id)
                self.CONFIG     = config
                self.__build_component()

        @staticmethod
        def __parse_cfg(config: dict | IInputForm):
                if type(config) == dict:
                        return Horizontal(
                                Input(placeholder=config["hint"], id="Search-field"),
                                Button(f"[{config['s_icon']}] Search", id="Search-button"),

                                id="Search-widget"
                        )
                elif type(config) == IInputForm:
                        return Horizontal(
                                Input(placeholder=config.HINT, id="Search-field"),
                                Button(f"[{config.SEARCH_ICON}] Search", id="Search-button"),

                                id="Search-widget"
                        )


        def __build_component(self):
                if self.CONFIG != None:
                        self.LAYOUT = Horizontal(
                                Input(placeholder="", id="Search-field"),
                                Button("[] Search", id="Search-button"),

                                id="Search-widget"
                        )
                else:
                        # Todo: Fix bug where defaults are not initialized
                        # Todo: Defaults system
                        self.LAYOUT = InputForm.__parse_cfg(InputForm.CONFIG)

        def compose(self):
                yield self.LAYOUT
