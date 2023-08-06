from textual.app import ComposeResult
from textual.widget import Widget
from textual.reactive import reactive
from textual.widgets import DirectoryTree, Static
from textual.containers import VerticalScroll, Vertical

from pathlib import Path
from typing import Iterable

from core.typedef import T_str, vec_T_str
from .InputForm import InputForm
from util.dev_utils import log

from .Table import TableHeader, TableEntry

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
        # Dependencies:
        # - InputForm.py
        # - Table.py

        # Alternating Color Scheme
        HEADER_BG_1   = TableHeader.HEADER_BG_1
        HEADER_BG_2   = TableHeader.HEADER_BG_2
        HEADER_FG     = TableHeader.HEADER_FG

        ENTRY_BG_1    = TableEntry.ENTRY_BG_1
        ENTRY_BG_2    = TableEntry.ENTRY_BG_2
        ENTRY_FG      = TableEntry.ENTRY_FG

        SEARCH_LABEL  = "Search"
        SEARCH_ICON   = ''

        SBOX_HINT     = "Directory Location:"
        SBOX_ICON     = ''


        def resolve(this, config: dict):
                def __nullish(value, default):
                        if      (value is None) or \
                                (value == "") or \
                                (value == '') or \
                                (value == ()):
                                return default
                        else:
                                return value

                def __color(scheme: dict):
                        for entry in scheme.keys():
                                match entry:
                                        case 'header_bg1':
                                                __nullish(scheme['header_bg1'],
                                                          ExplorerConfig.HEADER_BG_1)
                                        case 'header_bg2':
                                                __nullish(scheme['header_bg2'],
                                                          ExplorerConfig.HEADER_BG_2)
                                        case 'header_fg':
                                                __nullish(scheme['header_fg'],
                                                          ExplorerConfig.HEADER_FG)
                                        case 'entry_bg1':
                                                __nullish(scheme['entry_bg1'],
                                                          ExplorerConfig.ENTRY_BG_1)
                                        case 'entry_bg2':
                                                __nullish(scheme['entry_bg2'],
                                                          ExplorerConfig.ENTRY_BG_2)
                                        case 'entry_fg':
                                                __nullish(scheme['entry_fg'],
                                                          ExplorerConfig.ENTRY_FG)

                for key in config.keys():
                        match key:
                                case 'color_scheme':
                                        __color(config)

                                case 's_label':
                                        this.SEARCH_LABEL = (
                                                __nullish(config['s_label'],
                                                ExplorerConfig.SEARCH_LABEL)
                                        )

                                case 's_icon':
                                        this.SEARCH_ICON = (
                                                __nullish(config['s_icon'],
                                                ExplorerConfig.SEARCH_ICON)
                                        )

                                case 'sbox_label':
                                        this.SBOX_HINT = (
                                                __nullish(config['sbox_hint'],
                                                ExplorerConfig.SBOX_HINT)
                                        )

                                case 'sbox_icon':
                                        this.SBOX_ICON = (
                                                __nullish(config['sbox_icon'],
                                                ExplorerConfig.SBOX_ICON)
                                        )

        def parse_cfg(this, config: dict = None):
                this.resolve(config)

        def __init__(this, in_cfg: dict):
                this.parse_cfg(in_cfg)

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
