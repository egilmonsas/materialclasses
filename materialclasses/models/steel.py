from pydantic import BaseModel, Field, validator


class Steel(BaseModel):
    # Metainfo
    standard: str = Field(description="Governing design standard")
    variant: str = Field(description="Name of the steel class")

    # Material constants
    density: int = Field(description="Bulk density", default=7800, ge=0)
    E: int = Field(description="Youngs Modulus", default=210000)
    poisson: int = Field(description="Possion ratio", default=0.3, ge=0, le=1)
    G: int = Field(description="G", default=81000)

    # Strength parameters
    fy: int = Field(description="Yield strength, t<=40", ge=0)
    fu: int = Field(description="Ultimate strength, t<=40", ge=0)
    fy_t: int | None = Field(description="Yield strength, 40<t<=80", ge=0)
    fu_T: int | None = Field(description="Ultimate strength, 40<t<=80", ge=0)

    @validator("standard")
    def validate_standard(cls, v):
        if "NS-EN" not in v:
            raise ValueError('steel class must start with the letter "S"')
        return v

    @validator("variant")
    def validate_variant(cls, v):
        if v[0] != "S":
            raise ValueError('steel class must start with the letter "S"')
        return v
