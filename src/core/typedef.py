
from pathlib import Path
from typing import Literal

# = Types ===========================================================================

b_str           = str | Literal['']
T_str           = tuple[b_str, b_str]
vec_T_str       = list[T_str]


# = VFile ===========================================================================

class VFile:
        name: b_str
        css_id: b_str | int
        path: b_str | Path

        @staticmethod
        def __generate_id(collection: dict):
                len(collection)

        def __init(this,
                   entry: tuple[b_str | int, b_str,
                               b_str | Path],
                   collection: dict):

                this.css_id     = entry[1] if entry[1] is not None or '' \
                        else VFile.__generate_id(collection)
                this.name       = entry[0]
                this.path       = entry[2]

        def set_name(this, name: b_str):
                this.name       = name

        def set_id(this, id: b_str | int = None):
                this.css_id     = id

        def set_path(this, path: b_str | Path):
                this.path       = path

        def get_name(this) -> b_str:
                return this.name

        def get_id(this) -> b_str | int:
                return this.css_id

        def get_path(this) -> b_str | Path:
                return this.path

# = Store ===========================================================================

Store           = dict[b_str: VFile]
