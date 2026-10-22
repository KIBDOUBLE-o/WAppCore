from typing import Callable

from interface.interface_api import InterfaceApi


class ExampleIAPI(InterfaceApi):
    def __init__(self):
        super().__init__("Example")

    def show_text(self):
        self.call("showText")

    def set_text(self, text: str):
        self.call("setText", text)
