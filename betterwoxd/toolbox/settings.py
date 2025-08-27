"""___Modules_______________________________________________________________"""

import json

"""___Classes_______________________________________________________________"""

class Settings:

    test: bool

    def __init__(self, config: str = "prod") -> None:
        self.config_file = "settings.json"
        settings = self.load_settings()
        self.settings = settings[config]

        for key, value in self.settings.items():
            setattr(self, key, value)

    def load_settings(self):
        try:
            with open(self.config_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
