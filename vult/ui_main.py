from __future__ import annotations

# Textual TUI
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, RadioSet, RadioButton

# Modules

# Views
from vult.view.encoder_panel import EncoderDialogue
from vult.view.fm_panel import FileChooserDialogue

# Feature Set
# 1. Fetch source directory of videos
# 2. Select encoder & compression rate / ql strength
# 3. Select output directory 
# 4. Set optional encryption / security measures
# 5. Init parallelized encoding / compression (recommended: gnu parallel)
# 6. Show cool loading bar while waiting for dir | verbose encoding stats / logs



class EncoderSelectionWidget(Static):
        CSS_PATH = "radio_button.css"

        def compose(self) -> ComposeResult:
                with RadioSet():
                        yield RadioButton("NVENC H.265 (Fastest)", id="h265", value=True)
                        yield RadioButton("NVENC H.264", id="h264")
                        yield RadioButton("MPEG4", id="mpeg4")
                        yield RadioButton("AV1 (Slowest)", id="av1")

class Application(App[str]):

        def compose(self) -> ComposeResult:
                # DOM
                OptionsPanel    = EncoderDialogue()
                FilesPanel      = FileChooserDialogue()

                LAYOUT  = Horizontal(
                        Vertical(OptionsPanel,  id="EncoderSection"),
                        Vertical(FilesPanel,    id="FileChooserSection"),

                        id="Root",
                )
                yield LAYOUT

def init():
        app = Application(css_path="compress-scr.css")
        print(app.run())

# Program Entry Point -----
# if __name__ == '__main__':


