import json
from typing import Callable

import webview

from interface.windows_manager import WindowsManager


class UserInterface:
    def __init__(self, on_inited=lambda: None, on_loaded=lambda: None):
        self._api_functions: dict[str, Callable] = {}
        self.api = None

        self.on_inited = on_inited
        self.on_loaded = on_loaded

    def _contains_api_function(self, key: str) -> bool:
        return key in self._api_functions.keys()

    def _call_api_function(self, key: str, args: list):
        self._api_functions[key](*args)

    def register_api_function(self, key: str, function: Callable):
        if self._contains_api_function(key):
            print(f"API Function with key '{key}' already exists!")
            return
        self._api_functions[key] = function

    @staticmethod
    def call(target_window_name: str, function_name: str, args: list | None = None):
        if WindowsManager.is_opened(target_window_name):
            window = WindowsManager.get_window(target_window_name)
            js_args = [json.loads(arg) for arg in args] if args else []
            try:
                window.evaluate_js(f"{function_name}({', '.join(js_args)});")
            except Exception as e:
                print(f"JS Evaluation error: {e}")

    def on_loaded(self):
        self.on_loaded()

    def run(self):
        class Api:
            def call(api, key: str, args: list):
                self._call_api_function(key, args)

        self.api = Api()

        self.on_inited()

        webview.start(func=self.on_loaded)
