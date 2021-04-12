from app.models.settings_model import Settings
from app.factories.settings_factory import SettingsFactory
from app.storage import Storage
from fastapi import Depends
from json import dumps, loads

SETTINGS_KEY: str = 'settings'


class SettingsRepository:
    storage: Storage
    factory: SettingsFactory

    def __init__(self, storage: Storage = Depends(Storage), factory: SettingsFactory = Depends(SettingsFactory)):
        self.storage = storage
        self.factory = factory

    def save_settings(self, settings: Settings) -> Settings:
        self.storage.redis.set(
            SETTINGS_KEY,
            dumps(settings.dict())
        )

        return settings

    def get_settings(self) -> Settings:
        settings = self.storage.redis.get(SETTINGS_KEY)

        return self.factory.create(
            loads(settings) if settings else {}
        )
