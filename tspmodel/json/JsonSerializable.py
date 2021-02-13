from tspmodel.json.JsonTyping import Json_T


class JsonSerializable:
    """Interface JSON model"""

    def json(self) -> Json_T:
        """Returns the JSON (dict) representation"""
        pass
