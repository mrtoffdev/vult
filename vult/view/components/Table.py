from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Horizontal, Vertical

from vult.core.typedef import vec_T_str, L_str, vec_L_str
from vult.util.dev_utils import log

class TableEntry(Static):
        # Default Configuration
        ENTRY_BG_1    = "#303030"
        ENTRY_BG_2    = "#303030"
        ENTRY_FG      = "#FFFFFF"

        ICON_1          = "   "
        ICON_2          = ""

        # State
        VALUE           = ["Invalid Entry", "NaN"]

        # Layout Props
        ENTRY_ID        = VALUE[0]
        LAYOUT          = Static("TableEntry Layout err")

        def __init__(self, entry: L_str | None = None):
                self.parse_cfg(entry)
                super().__init__()

        def parse_cfg(self, entry: L_str | None = None):
                build = None
                match entry:
                        case entry if type(entry) is list:
                                build = entry
                        case None if type(entry) is None:
                                build = TableEntry.VALUE

                self.__build_component(build)

        def __build_component(self, entry: L_str | None):
                if type(entry) is L_str:
                        self.LAYOUT = Horizontal(
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
                        # id=str(entry[0].rstrip(".mp4"))
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
        HEADER_ICONSET  = [u'', u'']
        # HEADER_ICONSET  = [u'\ue64e', u'\ue706']
        HEADER_LABELSET: list = ["File Name:", "Size:"]

        # Layout
        LAYOUT          = Static("TableHeader layout err")

        def __init__(self, header: L_str | None):
                self.parse_cfg(header_set=header)
                super().__init__()

        def parse_cfg(self, header_set: L_str | None, icon_set: L_str | None = None):
                match header_set:
                        case header_set if type(header_set) == list:
                                self.HEADER_LABELSET = header_set
                        case None:
                                self.HEADER_LABELSET = TableHeader.HEADER_LABELSET

                match icon_set:
                        case icon_set if type(icon_set) == L_str:
                                self.HEADER_ICONSET = icon_set
                        case None:
                                self.HEADER_ICONSET = TableHeader.HEADER_ICONSET

                self.__build_component()

        def __build_component(self):
                self.LAYOUT = Horizontal(
                        # Static(f"{[self.HEADER_ICONSET[0]]} {this.HEADER_LABELSET[0]}",
                        #        classes="header-col1 fdir-cell-name"),
                        # Static(f"{[self.HEADER_ICONSET[1]]} {this.HEADER_LABELSET[1]}",
                        #        classes="header-col2 fdir-cell-size"),

                        classes="fdir-entry",
                )
                for i, header in enumerate(self.HEADER_LABELSET):

                        testss = Static(
                                        "[" + this.HEADER_ICONSET[i] + "] "
                                        f"{this.HEADER_LABELSET[i]}",
                                        "[" + self.HEADER_ICONSET[i] + "] "
                                        f"{header}",
                        )

                        if i == 0:
                                testss.add_class("header-col1")
                                testss.add_class("fdir-cell-name")
                        else:
                                testss.add_class("header-col2")
                                testss.add_class("fdir-cell-name")

                        self.LAYOUT.mount(
                                testss
                                # Static(
                                #         f"{[self.HEADER_ICONSET[i]]}"
                                #         f" {self.HEADER_LABELSET[i]}",
                                # )
                        )

        def compose(self) -> ComposeResult:
                yield self.LAYOUT


# Typing
TableConfig     = tuple[L_str, vec_L_str] | dict | None

class Table(Widget):

        # State
        TITLE           = reactive("")
        # HEADER          = reactive(["File Name:", "Size:"])
        HEADER          = ["File Name:", "Size:"]
        ENTRIES         = [
                ["", ""]
        ]

        SHOW_TITLE      = False
        SHOW_HEADER     = True

        LAYOUT          = Vertical()

        def __init__(self,
                     id: str,
                     config: TableConfig | dict | None = None):

                self.parse_cfg(config)
                super().__init__(id=id)

        def parse_cfg(self, config: TableConfig):
                # Config struct : <Header: L_str, Entries: vec_T_str>
                # T_TableSet = list[L_str, vec_T_str]

                if type(config) is list:

                        log("log", "Table __init__ rcvd valid config")

                        if (config[0] != []) or (config[0] is not None):
                                log("log", "received table data: " +
                                    str(config))
                                self.HEADER     = config[0]
                                self.ENTRIES    = config[1]
                else:

                        log("log", "Table __init__ rcvd invalid config")
                # elif type(config) is dict:
                #         pass
                #
                # elif type(config) is None:
                #         pass

                self.__build_component()

        def __build_component(self):
                HEADER_LAYOUT      = TableHeader(self.HEADER)
                TABLE_LAYOUT       = Vertical()

                # Dynamically mount entries
                for entry in self.ENTRIES:
                        if entry != ["", ""]:
                                TABLE_LAYOUT.mount(TableEntry(entry))
                self.LAYOUT.mount(HEADER_LAYOUT)
                self.LAYOUT.mount(TABLE_LAYOUT)

        def compose(self) -> ComposeResult:
                yield self.LAYOUT

        def set_data(self, data):
                self.ENTRIES = data

        def watch_ENTRIES(self, ENTRIES: list):
                pass

