from pydantic import baseSettings,SettingsConfigDict
class setting(baseSettings):

    APP_NAME : str
    APP_VERSION: str
    OPENAI_API_KEY: str
    class Config:
        env_file= ".env"
def   get_settings():
    return setting()   