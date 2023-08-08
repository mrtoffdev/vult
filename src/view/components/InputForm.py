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

                        case 'h_icon' if 'h_icon' in config.keys():
                                return __nullish(config['h_icon'],
                                                InputForm.CONFIG.HINT_ICON)

        def parse_cfg(this, config: dict | IInputForm):
                log("log", f"__parse rcvd: {str(config)}")

                # Dict initialization
                if type(config) == dict:
                        this.CONFIG = IInputForm(config)

                # Config initialization
                elif type(config) == IInputForm:

        def __init__(self, config=CONFIG, id=None):
                self.parse_cfg(config)
                super().__init__(id=id)


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
