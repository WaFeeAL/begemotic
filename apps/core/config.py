from pathlib import Path

from pydantic import BaseSettings, DirectoryPath, Field


class Settings(BaseSettings):
    ROOT_DIR: DirectoryPath = Field(
        Path(__file__).resolve().parent.parent.parent
    )
    DEBUG: bool = Field(False, env='DEBUG')
    DEFAULT_DATASET_NAME: str = Field(..., env='DEFAULT_DATASET_NAME')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
