import os.path


def get_key() -> str:
    if os.path.exists("key"):
        with open("key", "r", encoding="utf-8") as file:
            return file.read()
    else:
        raise OSError("Key file not exists!")
