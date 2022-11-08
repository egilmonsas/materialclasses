from pydantic import BaseModel, Field


class SolidTimber(BaseModel):
    # Metainfo
    standard: str = Field(description="Governing design standard", default="NS-EN 338:2016")
    variant: str = Field(description="Name of the solid timber class")

    # N/mm^2
    fm: int = Field(ge=0)
    ft_0: float = Field(ge=0)
    ft_90: float = Field(ge=0)
    fc_0: float = Field(ge=0)
    fc_90: float = Field(ge=0)
    fv: float = Field(ge=0)
    Em_0_mean: int = Field(ge=0)
    Em_0_k: int = Field(ge=0)
    Em_90_mean: int = Field(ge=0)
    G_mean: int = Field(ge=0)

    # kg/m^3
    density_k: int = Field(ge=0)
    density_mean: int = Field(ge=0)
