from typing import Type, TypeVar
from pydantic import BaseModel, SecretStr
from tomllib import load
from functools import lru_cache

ConfigType = TypeVar("ConfigType", bound=BaseModel)

class BotConfig(BaseModel):
    token: SecretStr

@lru_cache
def parse_config_file() -> dict:
    with open("config.toml", "rb") as file:
        return load(file)

@lru_cache
def get_config(model: Type[ConfigType], root_key: str) -> ConfigType:
    config_dict = parse_config_file()
    return model.model_validate(config_dict[root_key])