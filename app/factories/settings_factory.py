from app.models.settings_model import Settings
from typing import Dict


class SettingsFactory:

    def create(self, settings: Dict[str, str]) -> Settings:
        return Settings(
            business_name=settings.get('business_name', ''),
            address=settings.get('address', ''),
            zip_code=settings.get('zip_code', ''),
            phone=settings.get('phone', ''),
            fax=settings.get('fax', ''),
            vat_code=settings.get('vat_code', ''),
            city=settings.get('city', ''),
            province=settings.get('province', '')
        )
