"""
LA DISEÑADORA DE OUTFITS
Imagina que eres una diseñadora de moda virtual. Escribe un programa que recomiende un outfit basado en las condiciones del clima:
1) Si hace calor (temperatura > 30), recomienda ropa ligera y colorida.
2) Si está fresco, (temperatura <= 20 temperatura <= 30), sugiere algo casual y cómodo.
3) Si hace frío (temperatura < 20), propone abrigos y bufandas.

Extiende el programa usando una expresión ternaria para incluir un accesorio adicional:
a) Si hace sol (sol == True), agrega gafas de sol al outfit.
b) Si no, sugiere llevar un paraguas.

No te olvides de incorporar input()
"""

temperatura = int(input("Ingrese la temperatura actual: "))
sol = str(input("¿Hoy salió el sol? ¿S/N?: "))

hay_sol = "Lleva gafas de sol para protegerte de la luz solar~" if sol == "S" else "Te sugerimos llevar un paraguas, por si llueve~"

if temperatura >= 30:
    print(f"Te sugerimos usar ropa ligera y colorida ♥\n{hay_sol}")
elif temperatura >= 20 and temperatura < 30:
    print(f"Te sugerimos usar algo casual y cómodo ♥\n{hay_sol}")
else:
    print(f"Te sugerimos usar abrigo y bufanda ♥\n{hay_sol}")