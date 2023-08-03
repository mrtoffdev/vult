from textual.app import ComposeResult
from textual.widget import Widget
from textual.reactive import reactive
from textual.widgets import DirectoryTree, Static
from textual.containers import Horizontal, VerticalScroll, Vertical

# Todo: Refactor | Isolate to Core
from pathlib import Path
from typing import Iterable

from core.typedef import T_str, vec_T_str
from util.dev_utils import log

from .Table import TableHeader, TableEntry, Table

'''
        # Explorer Widget
        # Desc: The explorer widget is designed to take in a list of tuples,
                with each tuple serving as one entry, with an optional 
                constructor parameter that serves as a list of IDs for each
                entry.
                        (Default behavior takes entry[0], concatenates all
                        whitespace separated entries [if necessary], and uses
                        the result as an ID)
#       # Behavior: Dynamic. Blank Defaults
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


class Explorer(Widget):
        """
        # Explorer Widget
        An explorer widget is, by default, composed of two widgets that work together:
                1. Search Widget
                2. Table Widget

        The Search widget dictates the directory to be explored and iterated through by
        the Table widget. As such, it is more practical to have a separate widget for
        this collaborative function rather than having to create interfaces for each
        sub-widget manually in order to create the same effect
        """
        # Tree State
        TABLE_HEADER    = Static("Explorer Table Header Err")
        TABLE_ENTRIES  = reactive([])

        # Widget Layouts
        SEARCH_LAYOUT   = Static("Explorer Search Layout Err")
        TABLE_LAYOUT    = Static("Explorer Table Layout Err")

        LAYOUT          = Static("Explorer Root Layout err")

        # ===== DOM Operations =====

        def __init__(self, header: T_str, entries: vec_T_str, *children: Widget):
                super().__init__(*children)
                self.TABLE_HEADER       = TableHeader(header)
                self.TABLE_ENTRIES     = Table(entries)
                self.LAYOUT = Vertical(
                        self.TABLE_HEADER,
                        self.TABLE_LAYOUT,
                        *children,
                )

        def bind_entries(self, entries):
                self.TABLE_ENTRIES = entries

        def build(self) -> None:
                self.LAYOUT = Vertical(
                        self.SEARCH_LAYOUT,
                        self.TABLE_LAYOUT
                )

        # Render Blank Table
        def __build_component(self, header: T_str, entries: vec_T_str):
                # Build Header
                TEMP_HEADER = Static()
                if header != ("", ""):
                        TEMP_HEADER = TableHeader()
                        TEMP_HEADER.set_header(header)  # Set Default Header
                        TEMP_HEADER.classes = "w-fill"

                # Set init layout
                self.TABLE_HEADER = TEMP_HEADER
                self.TABLE_LAYOUT = VerticalScroll(classes="w-fill h-fill-p dbg-2")
                self.TABLE_LAYOUT.classes="table-fixed"

                log("log", f"entries: {str(entries)}")
                # Build Table
                for entry in entries:
                        if entry != ("", ""):
                                ENTRY = TableEntry(entry)
                                self.TABLE_LAYOUT.mount(ENTRY)

        def compose(self) -> ComposeResult:
                yield self.TABLE_HEADER
                yield self.TABLE_LAYOUT

        # State Mgmt
        def insert_entries(self, entries: tuple[type[str], type[str]]):
                self.TABLE_ENTRIES = entries

        def remove_entry(self, id: str):
                self.query_one('#' + id).remove()
