from fastapi import APIRouter, Depends
from app.models.settings_model import Settings
from app.repositories.settings_repository import SettingsRepository

settings_router = APIRouter()


@settings_router.get('/settings')
def settings(settings_repository: SettingsRepository = Depends(SettingsRepository)) -> Settings:
    return settings_repository.get_settings()


@settings_router.put('/settings')
def settings(settings: Settings, settings_repository: SettingsRepository = Depends(SettingsRepository)):
    return settings_repository.save_settings(settings)
