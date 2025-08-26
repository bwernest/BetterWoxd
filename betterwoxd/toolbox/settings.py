"""___Modules_______________________________________________________________"""

import json

"""___Classes_______________________________________________________________"""

class Settings:

    test: bool

    def __init__(self):
        self.config_file = "settings.json"
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open(self.config_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save_settings()

    def save_settings(self):
        with open(self.config_file, "w") as f:
            json.dump(self.settings, f, indent=4)
