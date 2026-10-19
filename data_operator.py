from crypto import Crypto


class DataOperator:
    @staticmethod
    def read(path: str) -> bytes:
        with open(path, "rb") as file:
            return file.read()

    @staticmethod
    def write(path: str, content: bytes):
        with open(path, "wb") as file:
            file.write(content)

    @staticmethod
    def read_encoded(path: str, key: str) -> bytes:
        return Crypto.decode(DataOperator.read(path), int(key, 16))

    @staticmethod
    def write_encoded(path: str, content: bytes, key: str):
        DataOperator.write(path, Crypto.encode(content, int(key, 16)))
