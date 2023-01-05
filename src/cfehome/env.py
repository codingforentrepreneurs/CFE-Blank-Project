import pathlib
from functools import lru_cache

from decouple import Config, RepositoryEnv

BASE_DIR = pathlib.Path(__file__).parent.parent

ENV_PATH = BASE_DIR / ".env"


@lru_cache()
def get_config():
    if ENV_PATH.exists():
        return Config(RepositoryEnv(ENV_PATH))
    from decouple import config

    return config


config = get_config()
