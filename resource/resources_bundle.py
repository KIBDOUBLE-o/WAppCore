import base64
import json

from data_operator import DataOperator
from resource.bundle_item import BundleItem


class ResourcesBundle:
    def __init__(self, encoding_key: str):
        self._header = {}
        self._content = {}
        self.encoding_key = encoding_key

    def set_header(self, header: dict) -> 'ResourcesBundle':
        self._header = header
        return self

    def create_category(self, category_name: str) -> 'ResourcesBundle':
        self._content[category_name] = {}
        return self

    def put(self, category_name: str, key: str, content: bytes) -> 'ResourcesBundle':
        if category_name not in self._content.keys():
            return self

        self._content[category_name][key] = base64.b64encode(content).decode()

        return self

    def is_available(self, category_name: str, key: str) -> bool:
        return category_name in self._content.keys() and key in self._content[category_name].keys()

    def take_encoded(self, category_name: str, key: str) -> BundleItem:
        if not self.is_available(category_name, key):
            return BundleItem.empty()

        return BundleItem(self._content[category_name][key])

    def take_decoded(self, category_name: str, key: str) -> BundleItem:
        if not self.is_available(category_name, key):
            return BundleItem.empty()

        return BundleItem(base64.b64decode(self.take_encoded(category_name, key).content).decode())

    def _final(self) -> dict:
        return {
            "header": self._header,
            "content": self._content
        }

    def _unpack(self, source: dict):
        self._header = source["header"]
        self._content = source["content"]

    def save(self, path: str):
        DataOperator.write_encoded(path, json.dumps(self._final()).encode(), self.encoding_key)

    def load(self, path: str) -> 'ResourcesBundle':
        self._unpack(json.loads(DataOperator.read_encoded(path, self.encoding_key)))
        return self

    @staticmethod
    def load_from(path: str, encoding_key: str) -> 'ResourcesBundle':
        return ResourcesBundle(encoding_key).load(path)
