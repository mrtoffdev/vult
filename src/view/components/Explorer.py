from textual.app import ComposeResult
from textual.widget import Widget
from textual.reactive import reactive
from textual.widgets import DirectoryTree, Static
from textual.containers import VerticalScroll, Vertical

from pathlib import Path
from typing import Iterable

from .InputForm import InputForm

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

class ExplorerLayout:
        # Dependencies:
        # - InputForm.py
        # - Table.py


        # Alternating Color Scheme
        HEADER_BG_1     = TableHeader.HEADER_BG_1
        HEADER_BG_2     = TableHeader.HEADER_BG_2
        HEADER_FG       = TableHeader.HEADER_FG

        ENTRY_BG_1      = TableEntry.ENTRY_BG_1
        ENTRY_BG_2      = TableEntry.ENTRY_BG_2
        ENTRY_FG        = TableEntry.ENTRY_FG


        # ----- Widget Exclusive -----

        # InputForm
        SF_TITLE        = "Video Sources Directory:"
        SF_BTN_SET      = ["Search", '']
        SF_FLD_SET      = ["Directory Location:", '']

        # Table
        TB_TITLE        = ""
        TB_HEADER       = ["File Name", "Size"]
        TB_ICON_SET     = ['', '']



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
                                        case 'hbg-1':
                                                __nullish(scheme['header_bg1'],
                                                          ExplorerLayout.HEADER_BG_1)
                                        case 'hbg-2':
                                                __nullish(scheme['header_bg2'],
                                                          ExplorerLayout.HEADER_BG_2)
                                        case 'hfg':
                                                __nullish(scheme['header_fg'],
                                                          ExplorerLayout.HEADER_FG)
                                        case 'ebg-1':
                                                __nullish(scheme['entry_bg1'],
                                                          ExplorerLayout.ENTRY_BG_1)
                                        case 'ebg-2':
                                                __nullish(scheme['entry_bg2'],
                                                          ExplorerLayout.ENTRY_BG_2)
                                        case 'efg':
                                                __nullish(scheme['entry_fg'],
                                                          ExplorerLayout.ENTRY_FG)

                for key in config.keys():
                        match key:
                                # Color
                                case 'color_scheme':
                                        __color(config['color_scheme'])

                                # InputForm Button -----

                                # Define as pair
                                case 'sfb_set':
                                        this.SF_BTN_SET = (
                                                __nullish(config['sfb_set'],
                                                          ExplorerLayout.SF_BTN_SET)
                                        )

                                # Define individually
                                case 's_icon':
                                        this.SF_BTN_SET[0] = (
                                                __nullish(config['s_icon'],
                                                          ExplorerLayout.SF_BTN_SET[0])
                                        )
                                case 's_label':
                                        this.SF_BTN_SET[1] = (
                                                __nullish(config['s_label'],
                                                          ExplorerLayout.SF_BTN_SET[1])
                                        )

                                # InputForm Field -----

                                # Define as pair
                                case 'sff_set':
                                        this.SF_FLD_SET = (
                                                __nullish(config['sff_set'],
                                                          ExplorerLayout.SF_FLD_SET)
                                        )

                                # Define individually
                                case 'sbox_icon':
                                        this.SF_FLD_SET[0] = (
                                                __nullish(config['sbox_icon'],
                                                          ExplorerLayout.SF_FLD_SET[0])
                                        )

                                case 'sbox_hint':
                                        this.SF_FLD_SET[1] = (
                                                __nullish(config['sbox_hint'],
                                                          ExplorerLayout.SF_FLD_SET[1])
                                        )

                                # Table
                                case 'table_header':
                                        pass

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

        DEFAULT_LAYOUT  = Vertical(
                InputForm(config={
                        "header"        : "Widget Header 1",
                        "hint"          : "Directory Search",
                        # "s_icon"        : '',
                        # "h_icon"        : ''
                })
        )

        CONFIG          = ExplorerLayout

        # State
        SW_TITLE        = reactive(str(""))     # Search Widget Header
        TW_TITLE        = reactive(str(""))     # Table Widget Header

        TABLE_HEADER    = reactive(("File Name", "Size"))
        TABLE_ENTRIES   = reactive([])

        # Widget Layouts
        SEARCH_LAYOUT   = Static()
        TABLE_LAYOUT    = Static()

        LAYOUT          = reactive(Static())

        # ===== DOM Operations =====

        def __init__(this,
                     config: ExplorerLayout | dict | None = None,
                     classes=None,
                     id=None, *children: Widget):

                super().__init__(*children, id=id, classes=classes)
                this.parse_cfg(config)

        def parse_cfg(this, config: ExplorerLayout | dict):
                if type(config) is dict:
                        this.CONFIG = ExplorerLayout(config)
                else:
                        this.CONFIG = config

                this.__build_component()

        def __build_component(this):
                # Build Header
                this.LAYOUT     = Vertical(
                        InputForm(),
                        VerticalScroll(classes="w-fill h-fill-p dbg-2 table-fixed")
                )

                # log("log", f"entries: {str(entries)}")
                # Build Table
                for entry in this.TABLE_ENTRIES:
                        if entry != ("", ""):
                                entry = TableEntry(entry)
                                this.TABLE_LAYOUT.mount(entry)

        # = State Mgmt ==============================================================

        def bind_entries(self, entries):
                self.TABLE_ENTRIES = entries

        def insert_entries(self, entries: tuple[type[str], type[str]]):
                self.TABLE_ENTRIES = entries

        def remove_entry(self, id: str):
                self.query_one('#' + id).remove()

        def compose(self) -> ComposeResult:
                yield self.LAYOUT
