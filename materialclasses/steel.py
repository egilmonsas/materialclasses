from materialclasses.models.steel_class import SteelClass

# fmt: off
classes = {
    "S 235":        SteelClass(standard="NS-EN 10025-2", variant="S 235", fy=235, fu=360, fy_t=215, fu_T=360),
    "S 275":        SteelClass(standard="NS-EN 10025-2", variant="S 275", fy=275, fu=430, fy_t=255, fu_T=410),
    "S 355":        SteelClass(standard="NS-EN 10025-2", variant="S 355", fy=355, fu=490, fy_t=335, fu_T=470),
    "S 450":        SteelClass(standard="NS-EN 10025-2", variant="S 450", fy=440, fu=550, fy_t=410, fu_T=550),
    "S 275 N/NL":   SteelClass(standard="NS-EN 10025-3", variant="S 275 N/NL", fy=275, fu=390, fy_t=255, fu_T=370),
    "S 355 N/NL":   SteelClass(standard="NS-EN 10025-3", variant="S 355 N/NL", fy=355, fu=490, fy_t=335, fu_T=470),
    "S 420 N/NL":   SteelClass(standard="NS-EN 10025-3", variant="S 420 N/NL", fy=420, fu=520, fy_t=390, fu_T=520),
    "S 460 N/NL":   SteelClass(standard="NS-EN 10025-3", variant="S 460 N/NL", fy=460, fu=540, fy_t=430, fu_T=540),
    "S 275 M/ML":   SteelClass(standard="NS-EN 10025-4", variant="S 275 M/ML", fy=275, fu=370, fy_t=255, fu_T=360),
    "S 355 M/ML":   SteelClass(standard="NS-EN 10025-4", variant="S 355 M/ML", fy=355, fu=470, fy_t=335, fu_T=450),
    "S 420 M/ML":   SteelClass(standard="NS-EN 10025-4", variant="S 420 M/ML", fy=420, fu=520, fy_t=390, fu_T=500),
    "S 460 M/ML":   SteelClass(standard="NS-EN 10025-4", variant="S 460 M/ML", fy=460, fu=540, fy_t=430, fu_T=530),
    "S 235 W":      SteelClass(standard="NS-EN 10025-5", variant="S 235 W", fy=235, fu=360, fy_t=215, fu_T=340),
    "S 355 W":      SteelClass(standard="NS-EN 10025-5", variant="S 355 W", fy=355, fu=490, fy_t=335, fu_T=490),
}
# fmt: on
