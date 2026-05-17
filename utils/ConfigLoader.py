import yaml
from pathlib import Path
# Config Settings
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config"

class ConfigLoader:

    @staticmethod
    def load_config():
        with open(CONFIG_FILE / "RoomConfig.yaml") as f:
            room_types = yaml.safe_load(f)

            return room_types.get("room_types",[])