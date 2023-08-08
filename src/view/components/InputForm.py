from textual.widgets import Static, Input, Button
from textual.containers import Horizontal, Vertical

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
        VALUE           = None

        # DOM
        ID              = None
        CSS_PATH        = None

        def __resolve(this, config: dict):
                def __nullish(value, default):
                        if      (value is None) or \
                                (value == "") or \
                                (value == '') or \
                                (value == ()):
                                return default
                        else:
                                return value

                for key in config.keys():
                        match key:
                                # Color
                                case 'fbg':
                                        this.FIELD_BG           = __nullish(config[key],
                                                                IInputForm.FIELD_BG)
                                case 'ffg':
                                        this.FIELD_FG           = __nullish(config[key],
                                                                IInputForm.FIELD_FG)
                                case 'title':
                                        this.TITLE              = __nullish(config[key],
                                                                IInputForm.TITLE)

                                # Submit Button
                                case 'sb-set':
                                        this.SBUTTON_SET        = __nullish(config[key],
                                                                IInputForm.SBUTTON_SET)
                                case 'sb-label':
                                        this.SBUTTON_SET[0]     = __nullish(config[key],
                                                                IInputForm.SBUTTON_SET[0])
                                case 'sb-icon':
                                        this.SBUTTON_SET[1]     = __nullish(config[key],
                                                                IInputForm.SBUTTON_SET[1])

                                # Input Field
                                case 'sf-set':
                                        this.SFIELD_SET         = __nullish(config[key],
                                                                IInputForm.SFIELD_SET)
                                case 'sf-label':
                                        this.SFIELD_SET[0]      = __nullish(config[key],
                                                                IInputForm.SFIELD_SET[0])
                                case 'sf-icon':
                                        this.SFIELD_SET[1]      = __nullish(config[key],
                                                                IInputForm.SFIELD_SET[1])

        def parse_cfg(this, config):
                this.__resolve(config)
        def __init__(this, config: dict) -> None:
                this.parse_cfg(config)
                # self.HEADER             = config["header"]
                # self.SEARCH_ICON        = config["s_icon"]
                # self.HINT               = config["hint"]
                # self.HINT_ICON          = config["h_icon"]

class InputForm(Static):
        
        CSS_PATH        = None
        CONFIG          = IInputForm(config={
                "header": "[] Default Header:",
                "s_icon": '',
                "hint"  : "[] Default Hint:",
                "h_icon": ''
        })

        LAYOUT          = Static("FSearchWidget.LAYOUT err")

        def parse_cfg(this, config: dict | IInputForm):
                log("log", f"__parse rcvd: {str(config)}")

                # Dict initialization
                if type(config) == dict:
                        this.CONFIG = IInputForm(config)

                # Config initialization
                elif type(config) == IInputForm:
                        this.CONFIG = config

        def __init__(self, config=CONFIG, id=None):
                self.parse_cfg(config)
                super().__init__(id=id)


        def __build_component(this):
                log("log", f"IForm __build()")
                this.LAYOUT = Vertical(
                        # Widget Header
                        Static(f"{this.CONFIG.TITLE}:",
                               classes="dialogue-header-top"),

                        # Input Form (Box + Button)
                        Horizontal(
                                Input(placeholder=f"[{this.CONFIG.SFIELD_SET[1]}"
                                                  f"]{this.CONFIG.SFIELD_SET[0]}",
                                        id="Search-field"),

                                Button(f"[{this.CONFIG.SBUTTON_SET[1]}] "
                                       f"{this.CONFIG.SBUTTON_SET[0]}",
                                        id="Search-button"),

                                id="Search-widget"
                        ),
                        classes="h-auto-w-fill"

                )

        def compose(self):
                yield self.LAYOUT
