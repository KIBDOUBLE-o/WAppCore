from typing import Callable

from interface.interface_api import InterfaceApi


class ExampleIAPI(InterfaceApi):
    show_text: Callable[[], None]
    set_text: Callable[[str], None]

    def __init__(self):
        super().__init__("Example", {
            "show_text": lambda api: api.call("showText"),
            "set_text": lambda api, text: api.call("setText", text)
        })
