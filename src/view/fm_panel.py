from core.typedef import vec_T_str

from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Vertical

from view.components.Explorer import Explorer

from util.dev_utils import log
from core.vult_core import Core

class FileChooserDialogue(Static):
        # State
        SOURCES: vec_T_str      = vec_T_str

        # DOM
        CSS_PATH                = "compress-scr.css"
        LAYOUT                  = Static()

        def rebuild_sources(self, source: str):
                self.SOURCES = Core.build_sources(source)

        def __construct(this):
                this.LAYOUT     = Vertical(
                        # Sources Explorer
                        Explorer(
                                classes="w-fill h-half-p",
                                id="source-panel"
                        ),

                        # Output Explorer
                        Explorer(
                                classes="w-fill h-half-p",
                                id="output-panel"
                        ),

                        classes="pad-s"
                )

        def __init__(self):
                super().__init__()
                log("log", "Init reached")

                self.rebuild_sources("./tests/")
                self.__construct()
                log("logfile.txt", self.SOURCES)

        def compose(self) -> ComposeResult:
                yield self.LAYOUT