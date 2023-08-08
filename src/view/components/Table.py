from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Horizontal, Vertical

from core.typedef import T_str, vec_T_str
from util.dev_utils import log

class TableEntry(Static):
        # Default Configuration
        ICON_1          = "   "
        ICON_2          = ""

        # State
        VALUE           = ("Invalid Entry", "NaN")

        # Layout Props
        ENTRY_ID        = VALUE[0]
        LAYOUT          = reactive(Static())

        def __init__(self, entry: T_str = None):
                self.parse_cfg(entry)
                super().__init__()

        def parse_cfg(self, entry: T_str):
                build = None
                match entry:
                        case entry if type(entry) == T_str:
                                build = entry
                        case None:
                                build = TableEntry.VALUE

                self.__build_component(build)

        def __build_component(this, entry: T_str | None):
                this.LAYOUT = Horizontal(
                        Static(
                                TableEntry.ICON_1 +
                                str(entry[0]),

                                classes="fdir-cell-name"
                        ),
                        Static(
                                TableEntry.ICON_2 +
                                str(entry[1]),

                                classes="fdir-cell-size"
                        ),

                        classes="fdir-entry",
                        id=str(entry[0].rstrip(".mp4"))
                )


        def compose(self) -> ComposeResult:
                yield self.LAYOUT


        #= State Mgmt ===============================================================

        def set_entry(self, entry: T_str) -> None:
                self.__build_component(entry)

class TableHeader(Static):
        # Header State
        ICON_1          = "[] "
        ICON_2          = "[] "

        DEFAULT         = ("Invalid Header", "NaN")

        # Layout Holder
        LAYOUT          = Static("TableHeader layout err")

        def __init__(self, header: T_str):
                self.parse_cfg(header)
                super().__init__()

        def parse_cfg(self, config: T_str):
                build = None
                match config:
                        case config if type(config) == T_str:
                                build = config
                        case None:
                                build = TableHeader.DEFAULT

                self.__build_component(build)

        def __build_component(self, config: T_str | None):
                self.LAYOUT = Horizontal(
                        Static(self.ICON_1 + str(config[0]),
                               classes="header-col1 fdir-cell-name"),
                        Static(self.ICON_2 + str(config[1]),
                               classes="header-col2 fdir-cell-size"),

                        classes="fdir-entry",
                )

        def compose(self) -> ComposeResult:
                yield self.LAYOUT


# Typing
TableConfig     = tuple[T_str, vec_T_str] | dict | None

class Table(Widget):

        # State
        TITLE           = ""
        HEADER          = reactive(("", ""))
        ENTRIES         = reactive([("", "")])

        WIDGET_HEADER   = Static()
        SHOW_HEADER     = False

        # DOM
        HEADER_LAYOUT   = Static()
        TABLE_LAYOUT    = Static()

        LAYOUT          = reactive(Static())

        def __init__(self, config: TableConfig, *children: Widget):
                self.parse_cfg(config)
                super().__init__(*children)

        def parse_cfg(this, config: TableConfig):
                match config:
                        # Tuple initialization
                        case config if type(config) == tuple[T_str, vec_T_str]:
                                this.HEADER = config[0] if (config[0] is not "" or
                                        config[0] is not None) else None

                        # Dict initialization
                        case config if type(config) == dict:
                                this.HEADER = config['header'] \
                                        if (config['header'] is not "" or
                                            config['header'] is not None) \
                                        else TableHeader.DEFAULT

                                this.ENTRIES = config['entries'] \
                                        if (config['entries'] is not "" or
                                            config['entries'] is not None) \
                                        else None

                this.__build_component()

        def __build_component(this, config=None):
                if config is None:
                        pass
                else:
                        this.HEADER_LAYOUT      = TableHeader(this.HEADER)
                        this.TABLE_LAYOUT       = Vertical()

                        # Dynamically mount entries
                        for entry in this.ENTRIES:
                                this.TABLE_LAYOUT.mount(TableEntry(entry=entry))

                        this.LAYOUT = Vertical (
                                this.HEADER_LAYOUT,
                                this.TABLE_LAYOUT
                        )


        def compose(self) -> ComposeResult:
                yield self.LAYOUT
