import webview
from webview import Window

from wac.interface.web_constructor import WebConstructor


class WindowsManager:
    _windows: dict[str, Window] = {}

    @classmethod
    def create_window(cls, name: str, constructor: WebConstructor, api, width=800, height=600, resizable=True, fullscreen=False, frameless=False, easy_drag=True, on_top=False):
        cls._windows[name] = webview.create_window(
            title=name,
            html=constructor.build(),
            js_api=api,
            width=width, height=height,
            resizable=resizable,
            fullscreen=fullscreen,
            frameless=frameless,
            easy_drag=easy_drag,
            on_top=on_top
        )

    @classmethod
    def get_window(cls, name: str) -> Window:
        return cls._windows[name]

    @classmethod
    def is_opened(cls, name: str) -> bool:
        return name in cls._windows.keys()

    @classmethod
    def someone_opened(cls) -> bool:
        return len(cls._windows) > 0

    @classmethod
    def terminate_window(cls, name: str):
        cls.get_window(name)
        del cls._windows[name]
