import json


class BundleItem:
    __slots__ = 'content'

    def __init__(self, content: str):
        self.content = content

    @staticmethod
    def empty() -> 'BundleItem':
        return BundleItem("")

    @property
    def as_dict(self) -> dict:
        return json.loads(self.content)

    @property
    def as_int(self):
        return int(self.content)

    @property
    def as_float(self):
        return float(self.content)
