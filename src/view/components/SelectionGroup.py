# Textual Packages
from textual.widgets import RadioButton, Static, RadioSet
from textual.app import ComposeResult

# Core
from core.typedef import vec_T_str

class SelectionGroup(Static):
        ERR_STR         = "SelectionGroup Error"

        CSS_PATH        = "radio_button.css"
        LAYOUT          = Static(ERR_STR)

        @staticmethod
        def new(widget_id: str, options: vec_T_str) -> RadioSet:
                build   = RadioSet(id=widget_id)
                for entry in options:
                        build.mount(RadioButton(entry[0], id=entry[1]))
                return build

        def compose(self) -> ComposeResult:
                yield self.LAYOUT
                # with RadioSet():
                #         yield RadioButton("NVENC H.265 (Fastest)",      id="h265", value=True)
                #         yield RadioButton("NVENC H.264",                id="h264")
                #         yield RadioButton("MPEG4",                      id="mpeg4")
                #         yield RadioButton("AV1 (Slowest)",              id="av1")

class EncoderSelectionWidget(Static):
        CSS_PATH = "radio_button.css"

        def compose(self) -> ComposeResult:
                with RadioSet():
                        yield RadioButton("NVENC H.265 (Fastest)",      id="h265", value=True)
                        yield RadioButton("NVENC H.264",                id="h264")
                        yield RadioButton("MPEG4",                      id="mpeg4")
                        yield RadioButton("AV1 (Slowest)",              id="av1")
