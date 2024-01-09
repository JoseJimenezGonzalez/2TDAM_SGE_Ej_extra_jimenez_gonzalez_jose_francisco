relaciones_tipos = {
    'Normal': {'Fuerte': [], 'Debil': ['Lucha']},
    'Lucha': {'Fuerte': ['Normal', 'Hielo', 'Roca', 'Acero', 'Siniestro'], 'Debil': ['Volador', 'Psíquico', 'Hada']},
    'Volador': {'Fuerte': ['Lucha', 'Bicho', 'Planta'], 'Debil': ['Eléctrico', 'Roca', 'Hielo']},
    'Veneno': {'Fuerte': ['Hada', 'Lucha'], 'Debil': ['Tierra', 'Psíquico']},
    'Tierra': {'Fuerte': ['Fuego', 'Roca', 'Acero'], 'Debil': ['Agua', 'Planta', 'Hielo']},
    'Roca': {'Fuerte': ['Fuego', 'Hielo', 'Volador', 'Bicho'], 'Debil': ['Agua', 'Planta', 'Lucha', 'Tierra']},
    'Bicho': {'Fuerte': ['Planta', 'Psíquico', 'Siniestro'], 'Debil': ['Fuego', 'Volador', 'Roca']},
    'Fantasma': {'Fuerte': ['Psíquico', 'Siniestro'], 'Debil': ['Normal', 'Lucha']},
    'Acero': {'Fuerte': ['Hielo', 'Roca', 'Hada'], 'Debil': ['Fuego', 'Lucha', 'Tierra']},
    'Fuego': {'Fuerte': ['Planta', 'Hielo', 'Bicho', 'Acero'], 'Debil': ['Agua', 'Roca', 'Fuego']},
    'Agua': {'Fuerte': ['Fuego', 'Tierra', 'Roca'], 'Debil': ['Planta', 'Eléctrico']},
    'Planta': {'Fuerte': ['Agua', 'Tierra', 'Roca'], 'Debil': ['Fuego', 'Hielo', 'Bicho']},
    'Eléctrico': {'Fuerte': ['Agua', 'Volador'], 'Debil': ['Tierra']},
    'Hielo': {'Fuerte': ['Planta', 'Tierra', 'Volador', 'Dragón'], 'Debil': ['Fuego', 'Lucha', 'Roca']},
    'Psíquico': {'Fuerte': ['Lucha', 'Veneno'], 'Debil': ['Bicho', 'Siniestro', 'Fantasma']},
    'Siniestro': {'Fuerte': ['Psíquico', 'Fantasma'], 'Debil': ['Lucha', 'Bicho', 'Hada']},
    'Dragón': {'Fuerte': ['Dragón'], 'Debil': ['Hielo', 'Hada', 'Roca']},
    'Hada': {'Fuerte': ['Lucha', 'Dragón', 'Siniestro'], 'Debil': ['Fuego', 'Veneno', 'Acero']},
}
ataques_no_afectan = {
    'Normal': ['Fantasma'],
    'Lucha': ['Volador'],
    'Fuego': [],
    'Agua': [],
    'Planta': [],
    'Eléctrico': ['Tierra'],
    'Hielo': [],
    'Tierra': ['Volador'],
    'Roca': [],
    'Volador': ['Tierra'],
    'Veneno': [],
    'Bicho': ['Fantasma'],
    'Fantasma': ['Normal'],
    'Psíquico': ['Siniestro'],
    'Siniestro': ['Psíquico'],
    'Acero': [],
    'Hada': [],
    'Dragón': [],
}
tipos_pokemon = ['Normal', 'Lucha', 'Fuego', 'Agua', 'Planta', 'Eléctrico', 'Hielo', 'Tierra', 'Roca', 'Volador', 'Veneno', 'Bicho', 'Fantasma', 'Psíquico', 'Siniestro', 'Acero', 'Hada', 'Dragón', 'Bicho']



def calcular_ventajas_desventajas(tipo_pokemon):
    tipo_pokemon = tipo_pokemon.capitalize()

    if tipo_pokemon in relaciones_tipos:
        fuerte_contra = relaciones_tipos[tipo_pokemon]['Fuerte']
        debil_contra = relaciones_tipos[tipo_pokemon]['Debil']

        return fuerte_contra, debil_contra
    else:
        return "Tipo de Pokémon no válido."


def calcular_ventajas_desventajas_doble_tipo(tipo1, tipo2=None):
    tipo1 = tipo1.capitalize()
    tipo2 = tipo2.capitalize() if tipo2 else None

    if tipo1 in relaciones_tipos and (tipo2 is None or tipo2 in relaciones_tipos):
        fuerte_contra_tipo1 = relaciones_tipos[tipo1]['Fuerte']
        debil_contra_tipo1 = relaciones_tipos[tipo1]['Debil']

        fuerte_contra_tipo2 = relaciones_tipos[tipo2]['Fuerte'] if tipo2 else []
        debil_contra_tipo2 = relaciones_tipos[tipo2]['Debil'] if tipo2 else []

        # Calcular fortalezas y debilidades combinadas
        fuerte_combinado = set(fuerte_contra_tipo1) & set(fuerte_contra_tipo2)
        debil_combinado = set(debil_contra_tipo1) & set(debil_contra_tipo2)
        if tipo2 == None:
            fuerte_combinado = fuerte_contra_tipo1
            debil_combinado = debil_contra_tipo1

        # Daño
        mensaje_danio = "Inflinge daño 4x: "
        for tipo in fuerte_combinado:
            mensaje_danio += f"{tipo}, "

        mensaje_danio = mensaje_danio[:-2] + ".\nInflinge daño 2x: "
        for tipo in tipos_pokemon:
            if tipo not in fuerte_combinado:
                mensaje_danio += f"{tipo}, "
        mensaje_danio = mensaje_danio[:-2] + ".\n"

        # Sufre
        mensaje_sufre = "Sufre daño 4x: "
        for tipo in debil_combinado:
            mensaje_sufre += f"{tipo}, "

        mensaje_sufre = mensaje_sufre[:-2] + ".\nSufre daño 2x: "
        for tipo in tipos_pokemon:
            if tipo not in debil_combinado and tipo not in ataques_no_afectan.get(tipo1, []) and tipo not in ataques_no_afectan.get(tipo2, []):
                mensaje_sufre += f"{tipo}, "
        mensaje_sufre = mensaje_sufre[:-2] + ".\n"

        # Ataques que no afectan
        tipos_no_afectados = set(ataques_no_afectan.get(tipo1, [])) | set(ataques_no_afectan.get(tipo2, []))
        mensaje_ataques_no_afectan = "Ataques que no afectan: " + ", ".join(tipos_no_afectados) + ".\n"

        return mensaje_danio + mensaje_sufre + mensaje_ataques_no_afectan

    else:
        return "Tipos de Pokémon no válidos."

# Modo Fácil
tipo_pokemon_facil = input("Ingrese el tipo de Pokémon (Modo Fácil): ")
resultados_facil = calcular_ventajas_desventajas(tipo_pokemon_facil)
print("Fuerte contra:", resultados_facil[0])
print("Débil contra:", resultados_facil[1])

# Modo Pro
tipo1_pro = input("Ingrese el primer tipo de Pokémon (Modo Pro): ")
tipo2_pro = input("Ingrese el segundo tipo de Pokémon (deje en blanco si el Pokémon tiene un solo tipo): ")

resultados_pro = calcular_ventajas_desventajas_doble_tipo(tipo1_pro, tipo2_pro)
print(resultados_pro)
