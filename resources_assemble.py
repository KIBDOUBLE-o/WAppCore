import json

from data_operator import DataOperator
from interface.web_constructor import WebConstructor
from resource.resources_bundle import ResourcesBundle
from utils import get_key

if __name__ == '__main__':
    bundle = ResourcesBundle(get_key())

    bundle.set_header({

    })

    bundle.create_category("interface")

    constructor = WebConstructor()

    constructor.include_index(DataOperator.read("resources/ui/index.html").decode())
    constructor.include_style(DataOperator.read("resources/ui/style.css").decode())
    constructor.include_script(DataOperator.read("resources/ui/script.js").decode())
    bundle.put("interface", "main", json.dumps(constructor.create_dump()).encode())

    bundle.save("resources.bundle")

