from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Horizontal, Vertical

from vult.core.typedef import vec_T_str, L_str

class TableEntry(Static):
        # Default Configuration
        ENTRY_BG_1    = "#303030"
        ENTRY_BG_2    = "#303030"
        ENTRY_FG      = "#FFFFFF"

        ICON_1          = "   "
        ICON_2          = ""

        # State
        VALUE           = ("Invalid Entry", "NaN")

        # Layout Props
        ENTRY_ID        = VALUE[0]
        LAYOUT          = reactive(Static())

        def __init__(self, entry: L_str = None):
                self.parse_cfg(entry)
                super().__init__()

        def parse_cfg(self, entry: L_str | None = None):
                build = None
                match entry:
                        case entry if type(entry) is L_str:
                                build = entry
                        case None if type(entry) is None:
                                build = TableEntry.VALUE

                self.__build_component(build)

        def __build_component(this, entry: L_str | None):
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

        def set_entry(self, entry: L_str) -> None:
                self.__build_component(entry)

class TableHeader(Static):
        # Color
        HEADER_BG_1     = "#444444"
        HEADER_BG_2     = "#303030"
        HEADER_FG       = "#FFFFFF"

        # Header State
        HEADER_ICONSET  = ['', '']
        HEADER_LABELSET: list = ["File Name:", "Size:"]

        # Layout
        LAYOUT          = Static("TableHeader layout err")

        def __init__(self, header: L_str | None):
                self.parse_cfg(header_set=header)
                super().__init__()

        def parse_cfg(this, header_set: L_str, icon_set: L_str = None):
                build = None
                match header_set:
                        case header_set if type(header_set) == L_str:
                                this.HEADER_LABELSET = header_set
                        case None:
                                this.HEADER_LABELSET = TableHeader.HEADER_LABELSET

                match icon_set:
                        case icon_set if type(icon_set) == L_str:
                                this.HEADER_ICONSET = icon_set
                        case None:
                                this.HEADER_ICONSET = TableHeader.HEADER_ICONSET

                this.__build_component()

        def __build_component(this):
                this.LAYOUT = Horizontal(
                        # Static(f"{[this.HEADER_ICONSET[0]]} {this.HEADER_LABELSET[0]}",
                        #        classes="header-col1 fdir-cell-name"),
                        # Static(f"{[this.HEADER_ICONSET[1]]} {this.HEADER_LABELSET[1]}",
                        #        classes="header-col2 fdir-cell-size"),

                        classes="fdir-entry",
                )
                for i, header in enumerate(this.HEADER_LABELSET):

                        testss = Static(
                                        f"{[this.HEADER_ICONSET[i]]} "
                                        f"{this.HEADER_LABELSET[i]}",
                        )

                        if i == 0:
                                testss.add_class("header-col1")
                                testss.add_class("fdir-cell-name")
                        else:
                                testss.add_class("header-col2")
                                testss.add_class("fdir-cell-name")

                        this.LAYOUT.mount(
                                testss
                                # Static(
                                #         f"{[this.HEADER_ICONSET[i]]}"
                                #         f" {this.HEADER_LABELSET[i]}",
                                # )
                        )

        def compose(self) -> ComposeResult:
                yield self.LAYOUT


# Typing
TableConfig     = tuple[L_str, vec_T_str] | dict | None

class Table(Widget):

        # State
        TITLE           = reactive("")
        HEADER          = reactive(["File Name:", "Size:"])
        ENTRIES         = reactive([
                ["", ""]
        ])

        SHOW_TITLE      = False
        SHOW_HEADER     = True

        # DOM
        HEADER_LAYOUT   = reactive(Static())
        TABLE_LAYOUT    = reactive(Static())

        LAYOUT          = reactive(Static("TablWidget.LAYOUT err"))

        def __init__(this,
                     config: TableConfig | dict | None = None,
                     *children: Widget):

                this.parse_cfg(config)
                super().__init__(*children)

        def parse_cfg(this, config: TableConfig):

                # Config struct : <Header: L_str, Entries: vec_T_str>
                T_TableSet = tuple[L_str, vec_T_str]

                if type(config) is T_TableSet:
                        if (config[0] != "") or (config[0] is not None):
                                this.HEADER = config[0]

                elif type(config) is dict:
                        pass

                elif type(config) is None:
                        pass

                this.__build_component()

        def __build_component(this):
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

