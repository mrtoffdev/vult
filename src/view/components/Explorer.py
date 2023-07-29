from textual.app import ComposeResult
from textual.widget import Widget
from textual.reactive import reactive
from textual.widgets import DirectoryTree, Static
from textual.containers import Horizontal, VerticalScroll, Vertical

# Todo: Refactor | Isolate to Core
from pathlib import Path
from typing import Iterable

from core.typedef import T_str, vec_T_str

'''
        # Explorer Widget
        # Desc: The explorer widget is designed to take in a list of tuples,
                with each tuple serving as one entry, with an optional 
                constructor parameter that serves as a list of IDs for each
                entry.
                        (Default behavior takes entry[0], concatenates all
                        whitespace separated entries [if necessary], and uses
                        the result as an ID)
'''

def __err():
        return "ExplorerConfig init err"

# Dir Tree Widget -------
class ExpFilter(DirectoryTree):
        def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
                return [path for path in paths if not path.name.startswith(".")]

class ExplorerConfig:
        # Structure
        __COLUMNS       = ""

        # Alternating Color Scheme
        __HEADER_BG_1   = ""
        __HEADER_BG_2   = ""
        __HEADER_FG     = "#FFFFFF"

        __ENTRY_BG_1    = ""
        __ENTRY_BG_2    = ""
        __ENTRY_FG      = "#FFFFFF"

        __SEARCH_LABEL  = ""
        __SEARCH_ICON   = ''

        __SBOX_HINT     = ""
        __SBOX_ICON     = ''


        # === Config Dict Reference: ===
        # -- code ----------------------
        # {
        #         # (Optional: Defaults supported)
        #         "color_scheme"  : {
        #                 "header_bg_1"   : str(hex),
        #                 "header_bg_2"   : str(hex),
        #                 "header_fg"     : str(hex),
        #
        #                 "entry_bg_1"    : str(hex),
        #                 "entry_bg_2"    : str(hex),
        #                 "entry_fg"      : str(hex),
        #         },
        #         "search_icon"   : char
        #         "search_label"  : str | char,
        #
        #         # (Non=Optional: Value of None in any will throw a non-crashing error)
        #         "header"        : "",
        #         "entries"       : vec_T_str
        # }
        def __init__(self, in_cfg: dict):
                # Todo: insert default values
                self.__HEADER_BG_1      = in_cfg["color_scheme"]["header_bg_1"] if \
                        in_cfg["color_scheme"]["header_bg_1"]   != "" else "Default"
                self.__HEADER_BG_2      = in_cfg["color_scheme"]["header_bg_2"] if \
                        in_cfg["color_scheme"]["header_bg_2"]   != "" else "Default"
                self.__HEADER_FG        = in_cfg["color_scheme"]["header_fg"] if \
                        in_cfg["color_scheme"]["header_fg"]     != "" else "Default"

                self.__ENTRY_BG_1       = in_cfg["color_scheme"]["entry_bg_1"] if \
                        in_cfg["color_scheme"]["entry_bg_1"]    != "" else "Default"
                self.__ENTRY_BG_2       = in_cfg["color_scheme"]["entry_bg_2"] if \
                        in_cfg["color_scheme"]["entry_bg_2"]    != "" else "Default"
                self.__ENTRY_FG         = in_cfg["color_scheme"]["entry_fg"] if \
                        in_cfg["color_scheme"]["entry_fg"]      != "" else "Default"

class TableEntry(Static):
        # Default Configuration
        ICON_1      = "   "
        ICON_2      = ""
        ENTRY_VALUE = ("", 0)
        ENTRY_ID    = ENTRY_VALUE[0]

        # Layout Holder
        LAYOUT = Static()

        def __init__(self, entry: T_str):
                super().__init__()
                self.LAYOUT = TableEntry.__build_component(entry)

        @staticmethod
        def __build_component(entry: T_str):
                return Horizontal(
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
                        id=str(entry[0])
                )

        @staticmethod
        def new(entry: T_str) -> Horizontal:
                return TableEntry.__build_component(entry)

        # Todo: (set_entry()) Figure out a better way of re-rendering
        #       the entry than rebuilding the whole component
        def set_entry(self, entry: T_str) -> None:
                self.LAYOUT = TableEntry.__build_component(entry)

        def compose(self) -> ComposeResult:
                if self.LAYOUT == ():
                        yield Static("Invalid Entry: Default Entry Spawned")
                else:
                        yield self.LAYOUT

class TableHeader(Static):
        # Header State
        ICON_1 = "[] "
        ICON_2 = "[] "

        # Layout Holder
        LAYOUT = Static()

        def compose(self) -> ComposeResult:
                if self.LAYOUT == ():
                        yield Static("Invalid Header: Default Header Spawned")
                else:
                        yield self.LAYOUT

        def set_header(self, header: T_str):
                self.LAYOUT = Horizontal(
                        Static(self.ICON_1 + str(header[0]), classes="header-col1 fdir-cell-name"),
                        Static(self.ICON_2 + str(header[1]), classes="header-col2 fdir-cell-size"),

                        classes="fdir-entry",
                )

class Table(Widget):
        '''
        # Table Widget
        '''
        LAYOUT          = Static()

        def compose(self) -> ComposeResult:
                yield self.LAYOUT

class Explorer(Widget):
        '''
        # Explorer Widget
        An explorer widget is, by default, composed of two widgets that work together:
                1. Search Widget
                2. Table Widget

        The Search widget dictates the directory to be explored and iterated through by
        the Table widget. As such, it is more practical to have a separate widget for 
        this collaborative function rather than having to create interfaces for each 
        sub-widget manually in order to create the same effect
        '''
        # Tree State
        TABLE_HEADER    = Static("Explorer Table Header Err")
        TABLE_CONTENTS  = reactive([])

        # Widget Layouts
        SEARCH_LAYOUT   = Static("Explorer Search Layout Err")
        TABLE_LAYOUT    = Static("Explorer Table Layout Err")

        # Widget Builder
        def build(self) -> Vertical:
                return Vertical(
                        self.SEARCH_LAYOUT,
                        self.TABLE_LAYOUT
                )

        # Render Blank Table
        def init_table(self, header: T_str, entries: vec_T_str):
                # Build Header
                TEMP_HEADER = Static()
                if header != ("", ""):
                        TEMP_HEADER = TableHeader()
                        TEMP_HEADER.set_header(header)  # Set Default Header
                        TEMP_HEADER.classes = "FCD-fs-header"

                # Set init layout
                self.TABLE_HEADER = TEMP_HEADER
                self.TABLE_LAYOUT = VerticalScroll(classes="FCD-fs-view")

                # Build Table
                for entry in entries:
                        if entry != ("", ""):
                                ENTRY = TableEntry()
                                ENTRY.set_entry(entry)
                                self.LAYOUT.mount(ENTRY)

        # State Mgmt
        def insert_entries(self, entries: tuple[type[str], type[str]]):
                self.TABLE_CONTENTS = entries

        def remove_entry(self, id: str):
                self.query_one('#' + id).remove()

        def compose(self) -> ComposeResult:
                yield self.TABLE_HEADER
                yield self.TABLE_LAYOUT
