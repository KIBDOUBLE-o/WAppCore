import base64
import json

from data_operator import DataOperator
from resource.bundle_item import BundleItem


class ResourcesBundle:
    def __init__(self, encoding_key: str):
        self._header = {}
        self._content = {}
        self.encoding_key = encoding_key

    def set_header(self, header: dict):
        self._header = header

    def create_category(self, category_name: str):
        self._content[category_name] = {}

    def put_in_category(self, category_name: str, key: str, content: bytes):
        if category_name not in self._content.keys():
            return

        self._content[category_name][key] = base64.b64encode(content).decode()

    def is_resource_available(self, category_name: str, key: str) -> bool:
        return category_name in self._content.keys() and key in self._content[category_name].keys()

    def take_from_category_encoded(self, category_name: str, key: str) -> BundleItem:
        if not self.is_resource_available(category_name, key):
            return BundleItem.empty()

        return BundleItem(self._content[category_name][key])

    def take_from_category_decoded(self, category_name: str, key: str) -> BundleItem:
        if not self.is_resource_available(category_name, key):
            return BundleItem.empty()

        return BundleItem(base64.b64decode(self.take_from_category_encoded(category_name, key).content).decode())

    def _final(self) -> dict:
        return {
            "header": self._header,
            "content": self._content
        }

    def _unpack(self, source: dict):
        self._header = source["header"]
        self._content = source["content"]

    def create_dump(self, path: str):
        DataOperator.write_encoded(path, json.dumps(self._final()).encode(), self.encoding_key)

    def load_dump(self, path: str):
        self._unpack(json.loads(DataOperator.read_encoded(path, self.encoding_key)))
