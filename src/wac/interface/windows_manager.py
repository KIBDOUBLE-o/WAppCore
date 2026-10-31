import webview
from webview import Window

from src.wac.interface.window_item import WindowItem

from src.wac.interface.web_constructor import WebConstructor


class WindowsManager:
    _windows: dict[str, WindowItem] = {}

    @classmethod
    def create_window(cls, name: str, constructor: WebConstructor, api, width=800, height=600, resizable=True, fullscreen=False, frameless=False, easy_drag=True, on_top=False):
        cls._windows[name] = WindowItem(webview.create_window(
            title=name,
            html=constructor.build(),
            js_api=api,
            width=width, height=height,
            resizable=resizable,
            fullscreen=fullscreen,
            frameless=frameless,
            easy_drag=easy_drag,
            on_top=on_top
        ))

    @classmethod
    def get_window(cls, name: str) -> Window:
        return cls._windows[name].window

    @classmethod
    def is_opened(cls, name: str) -> bool:
        return name in cls._windows.keys()

    @classmethod
    def someone_opened(cls) -> bool:
        return len(cls._windows) > 0

    @classmethod
    def terminate_window(cls, name: str):
        cls.get_window(name).destroy()
        del cls._windows[name]

    @classmethod
    def minimize_window(cls, name: str):
        cls.get_window(name).minimize()

    @classmethod
    def maximize_window(cls, name: str):
        cls._windows[name].is_maximized = not cls._windows[name].is_maximized
        if cls._windows[name].is_maximized:
            cls.get_window(name).maximize()
        else:
            cls.get_window(name).restore()
