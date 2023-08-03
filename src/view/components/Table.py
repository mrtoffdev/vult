from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Horizontal

from core.typedef import T_str

class TableEntry(Static):
        # Default Configuration
        ICON_1          = "   "
        ICON_2          = ""

        # State
        VALUE           = ("Invalid Entry", "NaN")

        # Layout Props
        ENTRY_ID        = VALUE[0]
        LAYOUT          = Static()

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
                if self.LAYOUT == ():
                        yield Static("Invalid Entry: Default Entry Spawned")
                else:
                        yield self.LAYOUT

        def set_entry(self, entry: T_str) -> None:
                self.LAYOUT = TableEntry.__build_component(entry)

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

class Table(Widget):
        """
        # Table Widget
        """
        LAYOUT          = Static()

        def compose(self) -> ComposeResult:
                yield self.LAYOUT
