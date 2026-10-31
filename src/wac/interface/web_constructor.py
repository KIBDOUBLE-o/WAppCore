class WebConstructor:
    __slots__ = ('_index', '_style', '_scripts')

    def __init__(self):
        self._index = []
        self._style = []
        self._scripts = []

    def include_index(self, index: str):
        self._index.append(index)

    def include_style(self, style: str):
        self._style.append(style)

    def include_script(self, script: str):
        self._scripts.append(script)

    def build(self) -> str:
        final = f"""
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <meta charset="utf-8">
                        <link rel="icon" href="icon.ico" type="image/png">
                    </head>
                    <style>
                    {'\n'.join(self._style)}
                    </style>
                    <body>
                    {'\n'.join(self._index)}
                    </body>
                    <script>
                    {'\n'.join(self._scripts)}
                    </script>
                    </html>
                    """
        return final

    def create_dump(self) -> dict:
        return {
            "index": self._index,
            "style": self._style,
            "script": self._scripts
        }

    def load_dump(self, dump: dict) -> 'WebConstructor':
        self._index = dump["index"]
        self._style = dump["style"]
        self._scripts = dump["script"]
        return self

    @staticmethod
    def load(dump: dict) -> 'WebConstructor':
        return WebConstructor().load_dump(dump)

    def clear(self):
        self._index = []
        self._style = []
        self._scripts = []
