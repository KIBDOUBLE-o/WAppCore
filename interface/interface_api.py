import json
from collections.abc import Callable

from interface.windows_manager import WindowsManager


class InterfaceApi:
    def __init__(self, window_name: str):
        self.window_name = window_name

    def call(self, function_name: str, *args):
        window = WindowsManager.get_window(self.window_name)
        if not window:
            return
        js_args = [json.dumps(arg) for arg in args] if args else []
        try:
            window.evaluate_js(f"{function_name}({', '.join(js_args)});")
        except Exception as e:
            print(f"JS Evaluation error: {e}")
