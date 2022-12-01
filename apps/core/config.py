from pathlib import Path

from pydantic import BaseSettings, DirectoryPath, Field


class Settings(BaseSettings):
    ROOT_DIR: DirectoryPath = Field(
        Path(__file__).resolve().parent.parent.parent
    )
    DEBUG: bool = Field(False, env='DEBUG')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
