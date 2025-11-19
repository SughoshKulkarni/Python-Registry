import json

from utils.registry import Data, register_exporter


@register_exporter("json")
def export_json(data: Data) -> None:
    print("Exporting data to JSON:")
    print(json.dumps(data, indent=2))
