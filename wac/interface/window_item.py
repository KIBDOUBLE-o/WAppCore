from webview import Window


class WindowItem:
    __slots__ = ('window', 'is_maximized')

    def __init__(self, window: Window):
        self.window = window
        self.is_maximized = False
