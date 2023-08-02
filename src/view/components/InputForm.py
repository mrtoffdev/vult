from textual.widgets import Static, Input, Button
from textual.containers import Horizontal, Vertical

from core.typedef import vec_T_str
from util.dev_utils import log


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

        @staticmethod
        def default():
                pass
        def __init__(self, config: dict) -> None:
                self.HEADER             = config["header"]
                self.SEARCH_ICON        = config["s_icon"]
                self.HINT               = config["hint"]
                self.HINT_ICON          = config["h_icon"]

class InputForm(Static):
        
        CSS_PATH        = None
        CONFIG          = IInputForm(config={
                "header": "[] Default Header:",
                "s_icon": '',
                "hint"  : "[] Default Hint:",
                "h_icon": ''
        })

        # Optional
        HEADER          = ""
        HINT            = ""

        LAYOUT          = Static("FSearchWidget.LAYOUT err")

        def __init__(self, config=CONFIG, id=None):
                super().__init__(id=id)
                self.CONFIG     = config
                self.__build_component()

        @staticmethod
        def __parse_cfg(config: dict | IInputForm):
                log("log", f"__parse rcvd: {str(config)}")
                if type(config) == dict:
                        return Vertical(
                                Static(f"{config['header']}:",
                                       classes="dialogue-header-top"),
                                Horizontal(
                                        Input(placeholder=config["hint"], id="Search-field"),
                                        Button(f"[{config['s_icon']}] Search", id="Search-button"),

                                        id="Search-widget"
                                ),
                                classes="h-auto-w-fill"

                        )
                elif type(config) == IInputForm:
                        return Vertical(
                                Static("Video Sources Directory:", classes="dialogue-header-top"),
                                Horizontal(
                                        Input(placeholder=config.HINT, id="Search-field"),
                                        Button(f"[{config.SEARCH_ICON}] Search", id="Search-button"),

                                        id="Search-widget"
                                ),
                                classes="h-auto-w-fill"
                        )


        def __build_component(self):
                log("log", f"IForm __build()")
                if self.CONFIG != None:
                        log("log", f"IForm __build(): has config: "
                                   f"XX")
                        self.LAYOUT = Horizontal(
                                Input(placeholder="", id="Search-field"),
                                Button("[] Search", id="Search-button"),

                                classes="w-fill",
                                id="Search-widget"
                        )
                else:
                        log("log", f"IForm __build(): no config")
                        # Todo: Fix bug where defaults are not initialized
                        # Todo: Defaults system
                        self.LAYOUT = InputForm.__parse_cfg(InputForm.CONFIG)

        def compose(self):
                yield self.LAYOUT
