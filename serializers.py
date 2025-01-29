from pydantic import BaseModel


class AutomobilisSchema(BaseModel):
    id: int
    gamintojas: str
    modelis: str
    spalva: str
    salis: str
    kaina: float

    class Config:
        from_attributes = True
