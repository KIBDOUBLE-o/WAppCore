import json

from example_iapi import ExampleIAPI
from interface.user_interface import UserInterface
from interface.web_constructor import WebConstructor
from interface.windows_manager import WindowsManager
from wac.resource import ResourcesBundle
from utils import get_key


class Example:
    def __init__(self):
        self.resources = ResourcesBundle.load_from("resources.bundle", get_key())


        self.ui = UserInterface(
            interface_api_interface=ExampleIAPI(),
            on_inited=self._on_inited,
            on_loaded=self._on_loaded
        )

        self._register_api()

        self.ui.run()

    @property
    def interface(self) -> ExampleIAPI:
        return self.ui.interface

    def _register_api(self):
        self.ui.register_api_function("print", lambda msg: print(f"JS MSG: {msg}"))

    def _on_inited(self):
        ui_item = self.resources.take_decoded("interface", "main")
        raw_dump = json.loads(ui_item.content)

        interface = WebConstructor.load(raw_dump)
        WindowsManager.create_window(
            name="Example",
            constructor=interface,
            api=self.ui.api
        )

    def _on_loaded(self):
        self.interface.set_text("Hi!")
        self.interface.show_text()


if __name__ == '__main__':
    example = Example()
