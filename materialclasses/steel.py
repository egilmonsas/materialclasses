from materialclasses.models.steel import Steel

# fmt: off
classes = {
    "S 235":            Steel(standard="NS-EN 10025-2", variant="S 235", fy=235, fu=360, fy_t=215, fu_T=360),
    "S 275":            Steel(standard="NS-EN 10025-2", variant="S 275", fy=275, fu=430, fy_t=255, fu_T=410),
    "S 355":            Steel(standard="NS-EN 10025-2", variant="S 355", fy=355, fu=490, fy_t=335, fu_T=470),
    "S 450":            Steel(standard="NS-EN 10025-2", variant="S 450", fy=440, fu=550, fy_t=410, fu_T=550),
    "S 275 N/NL":       Steel(standard="NS-EN 10025-3", variant="S 275 N/NL", fy=275, fu=390, fy_t=255, fu_T=370),
    "S 355 N/NL":       Steel(standard="NS-EN 10025-3", variant="S 355 N/NL", fy=355, fu=490, fy_t=335, fu_T=470),
    "S 420 N/NL":       Steel(standard="NS-EN 10025-3", variant="S 420 N/NL", fy=420, fu=520, fy_t=390, fu_T=520),
    "S 460 N/NL":       Steel(standard="NS-EN 10025-3", variant="S 460 N/NL", fy=460, fu=540, fy_t=430, fu_T=540),
    "S 275 M/ML":       Steel(standard="NS-EN 10025-4", variant="S 275 M/ML", fy=275, fu=370, fy_t=255, fu_T=360),
    "S 355 M/ML":       Steel(standard="NS-EN 10025-4", variant="S 355 M/ML", fy=355, fu=470, fy_t=335, fu_T=450),
    "S 420 M/ML":       Steel(standard="NS-EN 10025-4", variant="S 420 M/ML", fy=420, fu=520, fy_t=390, fu_T=500),
    "S 460 M/ML":       Steel(standard="NS-EN 10025-4", variant="S 460 M/ML", fy=460, fu=540, fy_t=430, fu_T=530),
    "S 235 W":          Steel(standard="NS-EN 10025-5", variant="S 235 W", fy=235, fu=360, fy_t=215, fu_T=340),
    "S 355 W":          Steel(standard="NS-EN 10025-5", variant="S 355 W", fy=355, fu=490, fy_t=335, fu_T=490),
    "S 460 Q/QL/QL1":   Steel(standard="NS-EN 10025-6", variant="S 355 W", fy=460, fu=570, fy_t=440, fu_T=550),
    "S 235 H":          Steel(standard="NS-EN 10021-1", variant="S 235 H", fy=235, fu=360, fy_t=215, fu_T=340),
    "S 275 H":          Steel(standard="NS-EN 10021-1", variant="S 275 H", fy=275, fu=430, fy_t=255, fu_T=410),
    "S 355 H":          Steel(standard="NS-EN 10021-1", variant="S 355 H", fy=355, fu=510, fy_t=335, fu_T=490),
    "S 275 NH/NLH":     Steel(standard="NS-EN 10021-1", variant="S 275 NH/NLH", fy=275, fu=390, fy_t=255, fu_T=370),
    "S 355 NH/NLH":     Steel(standard="NS-EN 10021-1", variant="S 355 NH/NLH", fy=355, fu=490, fy_t=335, fu_T=470),
    "S 420 NH/NLH":     Steel(standard="NS-EN 10021-1", variant="S 420 NH/NLH", fy=420, fu=540, fy_t=390, fu_T=520),
    "S 460 NH/NLH":     Steel(standard="NS-EN 10021-1", variant="S 460 NH/NLH", fy=460, fu=560, fy_t=430, fu_T=550),
}
# fmt: on
