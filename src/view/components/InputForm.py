from textual.widgets import Static, Input, Button
from textual.containers import Horizontal, Vertical

from core.typedef import vec_T_str
from util.dev_utils import log


class IInputForm:
        # Oolor
        FIELD_BG        = ""
        FIELD_FG        = ""

        # Layout
        TITLE           = Static("")
        SBUTTON_SET     = ['', "Search"]
        SFIELD_SET      = ['', "Source(s) Directory"]

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
                self.parse_cfg(config)
                super().__init__(id=id)

        # Helper for resolving config values & defaulting when null
        @staticmethod
        def __resolve(key: str, config: dict | IInputForm):
                def __nullish(value, default) :
                        if      (value is None) or \
                                (value == "") or \
                                (value == '') or \
                                (value == ()):
                                return default
                        else:
                                return value

                match key:
                        case 'header' if 'header' in config.keys():
                                return __nullish(config['header'],
                                                InputForm.CONFIG.HEADER)

                        case 's_icon' if 's_icon' in config.keys():
                                return __nullish(config['s_icon'],
                                                InputForm.CONFIG.SEARCH_ICON)

                        case 'hint' if 'hint' in config.keys():
                                return __nullish(config['hint'],
                                                InputForm.CONFIG.HINT)

                        case 'h_icon' if 'h_icon' in config.keys():
                                return __nullish(config['h_icon'],
                                                InputForm.CONFIG.HINT_ICON)

        def parse_cfg(this, config: dict | IInputForm):
                log("log", f"__parse rcvd: {str(config)}")

                # Dict initialization
                if type(config) == dict:
                        this.CONFIG.HEADER      = this.__resolve('header',
                                                                config=config)
                        this.CONFIG.HINT        = this.__resolve(key='hint',
                                                                config=config)
                        this.CONFIG.SEARCH_ICON = this.__resolve(key='s_icon',
                                                                config=config)
                        this.CONFIG.HINT_ICON   = this.__resolve(key='h_icon',
                                                                config=config)

                # Config initialization
                elif type(config) == IInputForm:

                        this.LAYOUT = Vertical(
                                Static("Video Sources Directory:", classes="dialogue-header-top"),
                                Horizontal(
                                        Input(placeholder=config.HINT, id="Search-field"),
                                        Button(f"[{config.SEARCH_ICON}] Search", id="Search-button"),

                                        id="Search-widget"
                                ),
                                classes="h-auto-w-fill"
                        )


        def __build_component(this):
                log("log", f"IForm __build()")
                this.LAYOUT = Vertical(
                        # Widget Header
                        Static(f"{this.CONFIG.HEADER}:",
                               classes="dialogue-header-top"),

                        # Input Form (Box + Button)
                        Horizontal(
                                Input(placeholder=f"[{this.CONFIG.HINT_ICON}"
                                                  f"]{this.CONFIG.HEADER}",
                                        id="Search-field"),
                                Button(f"[{this.CONFIG.SEARCH_ICON}] Search",
                                        id="Search-button"),

                                id="Search-widget"
                        ),
                        classes="h-auto-w-fill"

                )
                # if self.CONFIG != None:
                #         log("log", f"IForm __build(): has config: "
                #                    f"XX")
                #         self.LAYOUT = Horizontal(
                #                 Input(placeholder="", id="Search-field"),
                #                 Button("[] Search", id="Search-button"),
                #
                #                 classes="w-fill",
                #                 id="Search-widget"
                #         )
                # else:
                #         log("log", f"IForm __build(): no config")
                #         # Todo: Fix bug where defaults are not initialized
                #         # Todo: Defaults system
                #         self.LAYOUT = InputForm.__parse_cfg(InputForm.CONFIG)

        def compose(self):
                yield self.LAYOUT
