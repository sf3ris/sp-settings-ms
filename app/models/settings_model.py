from pydantic import BaseModel


class Settings(BaseModel):
    business_name: str
    address: str
    zip_code: str
    city: str
    province: str
    phone: str
    fax: str
    vat_code: str
