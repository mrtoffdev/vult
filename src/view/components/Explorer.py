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
                                # Color
                                case 'color_scheme':
                                        __color(config['color_scheme'])

                                # InputForm Button
                                case 's_icon':
                                        this.SBUTTON_SET[0] = (
                                                __nullish(config['s_icon'],
                                                          ExplorerConfig.SBUTTON_SET[0])
                                        )
                                case 's_label':
                                        this.SBUTTON_SET[1] = (
                                                __nullish(config['s_label'],
                                                ExplorerConfig.SBUTTON_SET[1])
                                        )

                                # InputForm Field
                                case 'sbox_icon':
                                        this.SFIELD_SET[0] = (
                                                __nullish(config['sbox_icon'],
                                                ExplorerConfig.SFIELD_SET[0])
                                        )

                                case 'sbox_hint':
                                        this.SFIELD_SET[1] = (
                                                __nullish(config['sbox_hint'],
                                                ExplorerConfig.SFIELD_SET[1])
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
                     id=None
                     ):
                super().__init__()

                this.classes    = classes if classes is not None else this.classes
                this.id         = id if id is not None else this.id
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
