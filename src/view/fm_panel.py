from core.typedef import vec_T_str

from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Container, Vertical

from view.components.InputForm import InputForm
from view.components.Explorer import Explorer

from util.dev_utils import log
from core.vult_core import Core

class FileChooserDialogue(Static):
        # State
        SOURCES: vec_T_str      = [("", "")]

        # DOM
        CSS_PATH                = "compress-scr.css"
        LAYOUT                  = Static()

        def rebuild_sources(self, source: str):
                self.SOURCES = Core.build_sources(source)

        def __init__(self):
                super().__init__()
                log("log", "Init reached")

                # Upper Section
                SOURCE_TREE     = Explorer()
                SOURCE_TREE.id  = "Source-dir"

                self.rebuild_sources("./tests/")
                log("logfile.txt", self.SOURCES)
                SOURCE_TREE.init_table((str("File Name"), str("Size")), self.SOURCES)


                # Lower Section
                OUT_TREE        = Explorer()
                OUT_TREE.id     = "Out-dir"

                OUT_TREE.init_table(("", ""), [("", "")])

                self.LAYOUT     = Container(
                        # Video Sources [Upper Section]
                        Vertical(
                                Static("Video Sources Directory:", classes="dialogue-header-top"),
                                InputForm(),
                                SOURCE_TREE,

                                classes="FCD-section",
                        ),

                        # Output & Statistics [Lower Section]
                        Vertical(
                                Static( "Output Directory:",
                                        classes="dialogue-header-sub"),
                                InputForm(),

                                Static("Results:",
                                        classes="dialogue-header-sub"),
                                OUT_TREE,

                                classes="FCD-section",
                        )
                )

        def compose(self) -> ComposeResult:
                yield self.LAYOUT