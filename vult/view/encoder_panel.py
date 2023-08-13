# Textual Packages
from textual import on
from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Button, Static, Select

# Package
from .components.SelectionGroup import EncoderSelectionWidget

class EncoderDialogue(Static):
        CSS_PATH = "compress-scr.css"

        PRESETS = [
                ("Preset 1 : [Fast Encode]", 1),
                ("Preset 2 : [High Compression]", 2),
                ("Preset 3 : [Lossless Transcode]", 3),
        ]

        QUALITY_SELECTION = [
                ("1 : [Lowest Quality]", 1),
                ("2 : [Low Quality]", 2),
                ("3 : [Medium Quality] (D)", 3),
                ("4 : [High Quality]", 4),
                ("5 : [Lossless Quality]", 5),
        ]

        TARGET_FORMAT = [
                ("MOV : [Quicktime Container]", "mov"),
                ("MP4 : [MPEG-4 Container] (D)", "mp4"),
                ("MKV : [Matroska Container]", "mkv"),
        ]

        LAYOUT          = Static("EncoderDialogue layout err")

        def __init__(self):
                super().__init__()
                self.LAYOUT = Container(
                        Static("Select Preset:", classes="dialogue-header-top"),

                        Select(self.PRESETS,
                               prompt="Select Preset:",
                               classes="full-width"
                               ),

                        Static("Select Encoder:", classes="dialogue-header-sub"),

                        EncoderSelectionWidget(),

                        # Button("NVENC H.265 (Fastest)", id="NVENC1"),
                        # Button("NVENC H.264", id="NVENC2"),
                        # Button("MPEG4", id="MPEG4"),
                        # Button("AV1 (Slowest)", id="AV1"),

                        Static("Select Quality Level: 1-5", classes="dialogue-header-sub"),

                        Select(self.QUALITY_SELECTION,
                               prompt="Quality (Default: 3)",
                               value=3,
                               classes="full-width"
                               ),

                        Static("Select Target Format:", classes="dialogue-header-sub"),

                        Select(self.TARGET_FORMAT,
                               prompt="Format (Default: MP4)",
                               value="mp4",
                               classes="full-width"
                               ),

                        Button("Encode Directory: (0 Files)", id="Encode-btn", disabled=True),

                        classes="pad-s"
                )

        def __build_component(this):
                pass
        def compose(self) -> ComposeResult:
                yield self.LAYOUT


        # ===== Events =====

        @on(Select.Changed)
        def select_changed(self, event: Select.Changed) -> None:
                self.title = str(event.value)


        def on_button_pressed(self, event: Button.Pressed) -> None:
                self.exit(str(event.button))
