from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Horizontal, Vertical

from core.typedef import T_str, vec_T_str

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
        # DOM
        HEADER_BG_1     = "#444444"
        HEADER_BG_2     = "#303030"
        HEADER_FG       = "#FFFFFF"

        # Header State
        HEADER_ICONSET  = ['', '']
        HEADER_LABELSET: list = ["File Name:", "Size:"]

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
                for i, header in enumerate(this.HEADER_LABELSET):

                        class_holder    = ""

                        if i == 0:
                                class_holder = "header-col1 fdir-cell-name"
                        else:
                                class_holder = "header-col2 fdir-cell-name"

                        testss = Static(
                                        f"{[this.HEADER_ICONSET[i]]} "
                                        f"{this.HEADER_LABELSET[i]}",
                                        classes=class_holder
                        )

                        testss.classes = class_holder

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
TableConfig     = tuple[T_str, vec_T_str] | dict | None

class Table(Widget):

        # State
        TITLE           = ""
        HEADER          = reactive(["File Name:", "Size:"])
        ENTRIES         = reactive([
                ["", ""]
        ])

        WIDGET_HEADER   = Static()
        SHOW_HEADER     = False

        # DOM
        HEADER_LAYOUT   = Static()
        TABLE_LAYOUT    = Static()

        LAYOUT          = reactive(Static("TablWidget.LAYOUT err"))

        def __init__(this,
                     config: TableConfig | dict | None = None,
                     *children: Widget):

                this.parse_cfg(config)
                super().__init__(*children)

        def parse_cfg(this, config: TableConfig):

                # Config struct : <Header: T_str, Entries: vec_T_str>
                T_TableSet = tuple[T_str, vec_T_str]

                if type(config) is T_TableSet:
                        if (config[0] != "") or (config[0] is not None):
                                this.HEADER = config[0]

                elif type(config) is dict:
                        pass

                elif type(config) is None:
                        pass

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
