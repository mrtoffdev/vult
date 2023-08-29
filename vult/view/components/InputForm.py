from textual.widgets import Static, Input, Button
from textual.containers import Horizontal, Vertical

from vult.util.dev_utils import log

class IInputForm:
        # Oolor
        FIELD_BG        = ""
        FIELD_FG        = ""

        # Layout
        TITLE           = "Directory Search"
        SBUTTON_SET     = ["Search",'']
        SFIELD_SET      = ["Source(s) Directory",'']

        # State
        VALUE           = None

        # DOM
        ID              = None
        CSS_PATH        = None

        def __resolve(self, config: dict[str, str]):
                def __nullish(value, default):
                        match value:
                                case None | "" | '' | ():
                                        return default
                                case _:
                                        return value

                for key in config.keys():
                        match key:
                                # Color
                                case 'fbg':
                                        self.FIELD_BG           = __nullish(config[key],
                                                                IInputForm.FIELD_BG)
                                case 'ffg':
                                        self.FIELD_FG           = __nullish(config[key],
                                                                IInputForm.FIELD_FG)
                                case 'title':
                                        self.TITLE              = __nullish(config[key],
                                                                IInputForm.TITLE)

                                # Submit Button
                                case 'sb-set':
                                        self.SBUTTON_SET        = __nullish(config[key],
                                                                IInputForm.SBUTTON_SET)
                                case 'sb-label':
                                        self.SBUTTON_SET[0]     = __nullish(config[key],
                                                                IInputForm.SBUTTON_SET[0])
                                case 'sb-icon':
                                        self.SBUTTON_SET[1]     = __nullish(config[key],
                                                                IInputForm.SBUTTON_SET[1])

                                # Input Field
                                case 'sf-set':
                                        self.SFIELD_SET         = __nullish(config[key],
                                                                IInputForm.SFIELD_SET)
                                case 'sf-label':
                                        self.SFIELD_SET[0]      = __nullish(config[key],
                                                                IInputForm.SFIELD_SET[0])
                                case 'sf-icon':
                                        self.SFIELD_SET[1]      = __nullish(config[key],
                                                                IInputForm.SFIELD_SET[1])

        def parse_cfg(self, config):
                self.__resolve(config)
        def __init__(self, config: dict[str, str]) -> None:
                self.parse_cfg(config)
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

        def parse_cfg(self, config: dict[str, str] | IInputForm):
                log("log", f"__parse rcvd: {str(config)}")

                # Dict initialization
                if type(config) is dict:
                        self.CONFIG = IInputForm(config)

                # Config initialization
                elif type(config) is IInputForm:
                        self.CONFIG = config

                elif type(config) is None:
                        self.CONFIG = InputForm.CONFIG

                self.__build_component()


        def __init__(self, config: dict[str,str] | IInputForm=CONFIG, id=None):
                self.parse_cfg(config)
                super().__init__(id=id)


        def __build_component(self):
                log("log", f"IForm __build()")
                self.LAYOUT = Vertical(
                        # Widget Header
                        Static(f"{self.CONFIG.TITLE}:",
                               classes="dialogue-header-top"),

                        # Input Form (Box + Button)
                        Horizontal(
                                Input(placeholder=f"[{self.CONFIG.SFIELD_SET[1]}] "
                                                  f"{self.CONFIG.SFIELD_SET[0]}",
                                        id="Search-field"),

                                Button(f"[{self.CONFIG.SBUTTON_SET[1]}] "
                                       f"{self.CONFIG.SBUTTON_SET[0]}",
                                        id="Search-button"),

                                id="Search-widget"
                        ),
                        classes="h-auto-w-fill"

                )

        def compose(self):
                yield self.LAYOUT
