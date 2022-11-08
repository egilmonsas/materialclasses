from materialclasses.models.solidtimber import SolidTimber

# fmt: off
classes = {
    "C14": SolidTimber(fm=14, ft_0=7.2, ft_90=0.4, fc_0=16, fc_90=2.0, fv=3.0, Em_0_mean=7000, Em_0_k=4700, G_mean=440, density_k=290, density_mean=350),
    "C16": SolidTimber(fm=16, ft_0=8.5, ft_90=0.4, fc_0=17, fc_90=2.2, fv=3.2, Em_0_mean=8000, Em_0_k=5400, G_mean=500, density_k=310, density_mean=370),
    "C18": SolidTimber(fm=18, ft_0=10.0,ft_90=0.4, fc_0=18, fc_90=2.2, fv=3.4, Em_0_mean=9000, Em_0_k=6000, G_mean=560, density_k=320, density_mean=380),
    "C20": SolidTimber(fm=20, ft_0=11.5,ft_90=0.4, fc_0=19, fc_90=2.3, fv=3.6, Em_0_mean=9500, Em_0_k=6400, G_mean=590, density_k=330, density_mean=400),
    "C22": SolidTimber(fm=22, ft_0=13.0,ft_90=0.4, fc_0=20, fc_90=2.4, fv=3.8, Em_0_mean=10000,Em_0_k=6700, G_mean=630, density_k=340, density_mean=410),
    "C24": SolidTimber(fm=24, ft_0=14.5,ft_90=0.4, fc_0=21, fc_90=2.5, fv=4.0, Em_0_mean=11000,Em_0_k=7400, G_mean=690, density_k=350, density_mean=420),
    "C27": SolidTimber(fm=27, ft_0=16.5,ft_90=0.4, fc_0=22, fc_90=2.5, fv=4.0, Em_0_mean=11500,Em_0_k=7700, G_mean=720, density_k=360, density_mean=430),
    "C30": SolidTimber(fm=30, ft_0=19.0,ft_90=0.4, fc_0=24, fc_90=2.7, fv=4.0, Em_0_mean=12000,Em_0_k=8000, G_mean=750, density_k=380, density_mean=460),
    "C35": SolidTimber(fm=35, ft_0=22.5,ft_90=0.4, fc_0=25, fc_90=2.7, fv=4.0, Em_0_mean=13000,Em_0_k=8700, G_mean=810, density_k=390, density_mean=470),
    "C40": SolidTimber(fm=40, ft_0=26.0,ft_90=0.4, fc_0=27, fc_90=2.8, fv=4.0, Em_0_mean=14000,Em_0_k=9400, G_mean=880, density_k=400, density_mean=480),
    "C45": SolidTimber(fm=45, ft_0=30.0,ft_90=0.4, fc_0=29, fc_90=2.9, fv=4.0, Em_0_mean=15000,Em_0_k=10100,G_mean=940, density_k=410, density_mean=490),
    "C50": SolidTimber(fm=50, ft_0=33.5,ft_90=0.4, fc_0=30, fc_90=3.0, fv=4.0, Em_0_mean=16000,Em_0_k=10700,G_mean=1000,density_k=430, density_mean=520),
}
# fmt: on
