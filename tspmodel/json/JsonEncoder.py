from json import JSONEncoder
from tspmodel.json.JsonTyping import Json_T
from tspmodel.json.JsonSerializable import JsonSerializable


class JsonEncoder(JSONEncoder):
    """Formatter for dump a JSON object"""

    def default(self, o: JsonSerializable) -> Json_T:
        return o.json()
