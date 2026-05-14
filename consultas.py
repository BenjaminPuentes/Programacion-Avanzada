from backend.nodo_ligado import NodoLigado
from typing import Generator
from utils import (HabitatObjeto, Juguete, JugueteHabitat, JugueteObjeto, JugueteRecurso, 
                   ObjetoRecurso, PeriodoDia, RecursoRecurso)

def cargar_juguete(path: str) -> Generator[Juguete, None, None]:
    with open(path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea= linea.strip()
            id_juguete, nombre, afinidades, sprite = linea.split(',')
            lista_afinidades = []
            for afinidad in afinidades.split(';'):
                lista_afinidades.append(int(afinidad))
            afinidades = tuple(lista_afinidades)
            yield Juguete(int(id_juguete), nombre, afinidades, sprite)

def cargar_juguete_habitat(path: str) -> Generator[JugueteHabitat, None, None]:
    with open(path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            id_juguete, id_habitat, tiempo_espera, periodos = linea.split(',')
            lista_periodos = []
            for periodo in periodos.split(';'):
                lista_periodos.append(int(periodo))
            ids_periodo_dia = tuple(lista_periodos)
            yield JugueteHabitat(int(id_juguete), int(id_habitat), tiempo_espera, ids_periodo_dia)

def cargar_habitat_objeto(path: str) -> Generator[HabitatObjeto, None, None]:
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            id_habitat, objetos = linea.split(",")
            objetos_lista = []
            for objeto in objetos.split(";"):
                if objeto != "":
                    id_objeto, cantidad = objeto.split(":")
                    objetos_lista.append((int(id_objeto), int(cantidad)))
            objetos_tupla = tuple(objetos_lista)
            yield HabitatObjeto(int(id_habitat), objetos_tupla)

def cargar_objeto_recurso(path: str) -> Generator[ObjetoRecurso, None, None]:
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            id_objeto, recursos = linea.split(",")
            recursos_lista = []
            for recurso in recursos.split(";"):
                if recurso != "":
                    id_recurso, cantidad = recurso.split(":")
                    recursos_lista.append((int(id_recurso), int(cantidad)))
            recursos_tupla = tuple(recursos_lista)
            yield ObjetoRecurso(int(id_objeto), recursos_tupla)

def cargar_recurso_recurso(path: str) -> Generator[RecursoRecurso, None, None]:
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            id_recurso, recursos, id_afinidad = linea.split(",")
            recursos_lista = []
            for recurso in recursos.split(";"):
                if recurso != "":
                    id_recurso_v2, cantidad = recurso.split(":")
                    recursos_lista.append((int(id_recurso_v2), int(cantidad)))
            recursos_tupla = tuple(recursos_lista)
            yield RecursoRecurso(int(id_recurso), recursos_tupla, int(id_afinidad))

def cargar_juguete_recurso(path: str) -> Generator[JugueteRecurso, None, None]:
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            id_juguete, id_recurso, tiempo_espera, cantidad = linea.split(',')
            yield JugueteRecurso(int(id_juguete), int(id_recurso), tiempo_espera, int(cantidad))

def cargar_juguete_objeto(path: str) -> Generator[JugueteObjeto, None, None]:
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            id_juguete, id_objeto = linea.split(',')
            yield JugueteObjeto(int(id_juguete), int(id_objeto))

def cargar_periodo_dia(path: str) -> Generator[PeriodoDia, None, None]:
    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            id_periodo_dia, nombre, duracion = linea.split(',')
            yield PeriodoDia(int(id_periodo_dia), nombre, duracion)

def ahora_es(generador_perio_dia: Generator, minutos: int) -> tuple:
    periodos = list(generador_perio_dia)
    minutos_totales_dia = 0
    for periodo in periodos:
        horas, min = periodo.duracion.split(":")
        minutos_totales_dia += (int(horas) * 60 + int(min))
    dia_actual = minutos // minutos_totales_dia
    minutos_del_dia = minutos % minutos_totales_dia
    hora = minutos_del_dia // 60
    minuto_actual = minutos_del_dia % 60
    hora_actual = f"{hora:02}:{minuto_actual:02}"
    minuto_inicio = 0
    for periodo in periodos:
        horas, min = periodo.duracion.split(":")
        duracion = (int(horas) * 60 + int(min))
        minuto_fin = minuto_inicio + duracion
        if minuto_inicio <= minutos_del_dia < minuto_fin:
            inicio_hora = minuto_inicio // 60
            inicio_minuto = minuto_inicio % 60
            fin_hora = minuto_fin // 60
            fin_minuto = minuto_fin % 60 
            hora_inicio = f"{inicio_hora:02}:{inicio_minuto:02}"
            hora_fin = f"{fin_hora:02}:{fin_minuto:02}"
            return (dia_actual, hora_actual, periodo.nombre, hora_inicio, hora_fin)
        minuto_inicio = minuto_fin

def recursos_a_partir_de_recurso(generador_recurso_recurso: Generator,
                                 id_recurso: int) -> Generator:
    
    # 1. Convertimos y ordenamos de menor a mayor
    lista_rr = list(generador_recurso_recurso)
    lista_rr.reverse()
    
    # fabricables = {id: (set_afinidades, cantidad_acumulada)}
    fabricables = {id_recurso: (set(), 1)}
    resultados = {}
    
    for receta in lista_rr:
        
        # Filtramos los ingredientes de la receta que ya somos capaces de fabricar
        ingredientes_validos = list(filter(
            lambda req: req[0] in fabricables, 
            receta.recursos
        ))
        
        # EL CAMBIO CLAVE: Para fabricar un recurso, necesitamos poseer
        # TODOS los ingredientes que pide su receta, no solo una parte de ellos.
        if len(ingredientes_validos) == len(receta.recursos):
            nuevas_afinidades = set()
            nueva_cantidad_total = 0
            
            # Iteramos sobre los ingredientes válidos para sumar los aportes
            for id_ing, cant_requerida_por_receta in ingredientes_validos:
                afinidades_previas, cant_acumulada_ing = fabricables[id_ing]
                
                # Sumamos la cantidad matemática de este camino
                nueva_cantidad_total += cant_acumulada_ing * cant_requerida_por_receta
                
                # Unimos las afinidades del camino
                for af in afinidades_previas:
                    nuevas_afinidades.add(af)
                    
            # Sumamos la afinidad propia de la receta final
            nuevas_afinidades.add(receta.id_afinidad)
            
            # Guardamos el resultado exitoso
            fabricables[receta.id_recurso] = (nuevas_afinidades, nueva_cantidad_total)
            resultados[receta.id_recurso] = (nuevas_afinidades, nueva_cantidad_total)
            
    # Retornamos formateado a tu estilo
    yield from map(
        lambda x: (x, tuple(sorted(resultados[x][0])), resultados[x][1]), 
        sorted(resultados)
    )
    



    

    # dependencias = {}

    # for relacion in generador_recurso_recurso:
    #     for recurso_necesario, cantidad in relacion.recursos:
    #         if recurso_necesario not in dependencias:
    #             dependencias[recurso_necesario] = []

    #         dependencias[recurso_necesario].append((relacion.id_recurso, relacion.id_afinidad, cantidad))

    # resultados = {}
    # stack = [(id_recurso, set(), 1)]
    # while stack:

    #     recurso_actual, afinidades, cantidad_total = stack.pop()

    #     if recurso_actual not in dependencias:
    #         continue

    #     for id_resultante, afinidad, cantidad in \
    #             dependencias[recurso_actual]:

    #         nuevas_afinidades = afinidades | {afinidad}
    #         nueva_cantidad = cantidad_total * cantidad

    #         if id_resultante not in resultados:
    #             resultados[id_resultante] = [set(), 0]

    #         resultados[id_resultante][0].update(nuevas_afinidades)

    #         resultados[id_resultante][1] += nueva_cantidad

    #         stack.append((id_resultante, nuevas_afinidades, nueva_cantidad))

    # yield from map(
    #     lambda x: (x, tuple(sorted(resultados[x][0])), resultados[x][1]), sorted(resultados)
    #     )

def juguetes_producen(generador_juguete_recurso: Generator, id_recurso: int) -> Generator:

    # 1. Filtramos de forma perezosa los registros que producen el recurso solicitado
    filtrados = filter(
        lambda jr: jr.id_recurso == id_recurso,
        generador_juguete_recurso
    )

    # 2. Mapeamos para quedarnos únicamente con los IDs de los juguetes
    ids = map(
        lambda jr: jr.id_juguete,
        filtrados
    )

    # 3. Entregamos los resultados directamente. 
    # Al estar el CSV ordenado por id_juguete y tener un recurso único por juguete,
    # garantizamos que saldrán ordenados de menor a mayor y sin repetidos.
    for id_juguete in ids:
        yield id_juguete



    # filtrados = filter(
    #     lambda x: x.id_recurso == id_recurso,
    #     generador_juguete_recurso
    # )

    # ids = map(
    #     lambda x: x.id_juguete,
    #     filtrados
    # )

    # vistos = set()

    # for id_juguete in ids:

    #     if id_juguete not in vistos:

    #         vistos.add(id_juguete)

    #         yield id_juguete
    pass


def juguetes_productivos(generador_juguete_recurso: Generator,
                         minimo: float | None = None) -> Generator:
    
    if minimo is not None:
        # CASO 1: Con umbral. 
        # Evaluamos de forma perezosa (O(1) memoria) aplicando filter al generador.
        filtrados = filter(
            lambda j: (j.cantidad / (int(j.tiempo_espera.split(':')[0]) * 60 + 
                                     int(j.tiempo_espera.split(':')[1]))) > minimo, 
            generador_juguete_recurso
        )
        
        # Mapeamos para extraer únicamente los IDs
        ids_filtrados = map(lambda j: j.id_juguete, filtrados)
        
        for id_jug in ids_filtrados:
            yield id_jug
            
    else:
        # CASO 2: Sin umbral (Encontrar el máximo).
        # Aquí sí debemos consumir el generador, pero para ahorrar memoria
        # lo mapeamos directamente a tuplas simples: (id_juguete, productividad).
        productividades = list(map(
            lambda j: (j.id_juguete, 
                       j.cantidad / (int(j.tiempo_espera.split(':')[0]) * 60 + 
                                     int(j.tiempo_espera.split(':')[1]))),
            generador_juguete_recurso
        ))
        
        if not productividades:
            return
            
        # Extraemos el valor máximo usando map sobre nuestra lista
        max_valor = max(map(lambda prod: prod[1], productividades))
        
        # Filtramos solo aquellos juguetes que empaten con el valor máximo
        mejores = filter(lambda prod: prod[1] == max_valor, productividades)
        
        # Mapeamos para entregar solo el ID de los que pasaron el filtro
        ids_mejores = map(lambda prod: prod[0], mejores)
        
        for id_jug in ids_mejores:
            yield id_jug
    


    # lista_juguetes = list(generador_juguete_recurso)
    
    # if not lista_juguetes:
    #     return (id for id in [])

    # # Lógica de cálculo de productividad: (cantidad / minutos_totales)
    # # Usamos una lambda directamente donde se necesite
    
    # if minimo is not None:
    #     # Caso con umbral: usamos filter con una lambda que hace el cálculo in-line
    #     filtrados = filter(
    #         lambda j: (j.cantidad / (int(j.tiempo_espera.split(':')[0]) * 60 + 
    #                                  int(j.tiempo_espera.split(':')[1]))) > minimo, 
    #         lista_juguetes
    #     )
    #     yield from (j.id_juguete for j in filtrados)
    
    # else:
    #     # Caso None: Encontrar el máximo
    #     # 1. Creamos una lista de productividades para usar max()
    #     productividades = [
    #         (j.id_juguete, j.cantidad / (int(j.tiempo_espera.split(':')[0]) * 60 + 
    #                                      int(j.tiempo_espera.split(':')[1])))
    #         for j in lista_juguetes
    #     ]
        
    #     # 2. Obtenemos el valor máximo de las productividades calculadas
    #     max_valor = max(prod[1] for prod in productividades)
        
    #     # 3. Retornamos todos los IDs que coincidan con ese máximo
    #     yield from (id for id, valor in productividades if valor == max_valor)


def habitats_de_interes(generador_juguete: Generator,
                        generador_juguete_habitat: Generator) -> Generator:
    
    # 1. Obtenemos los IDs de los juguetes que ya están en el refugio.
    # Usamos map para extraer solo el id_juguete del generador.
    juguetes_aparecidos = set(map(lambda j: j.id_juguete, generador_juguete))
    
    # 2. Filtramos el generador para dejar solo los juguetes que AÚN NO han aparecido.
    relaciones_pendientes = filter(
        lambda jh: jh.id_juguete not in juguetes_aparecidos, 
        generador_juguete_habitat
    )
    
    # 3. Mapeamos las relaciones para quedarnos únicamente con los IDs de los hábitats.
    ids_habitats_pendientes = map(lambda jh: jh.id_habitat, relaciones_pendientes)
    
    # 4. Iteramos y entregamos los resultados sin usar sorted() ni sets adicionales.
    # Como los datos base ya vienen ordenados por id_habitat, basta con 
    # recordar el último que entregamos para no repetir.
    ultimo_habitat_entregado = None
    
    for id_habitat in ids_habitats_pendientes:
        if id_habitat != ultimo_habitat_entregado:
            yield id_habitat
            ultimo_habitat_entregado = id_habitat


    # juguetes_aparecidos = {j.id_juguete for j in generador_juguete}
    
    # # 2. Filtramos el generador de JugueteHabitat.
    # # Nos interesan las entradas donde el juguete NO está en el set de aparecidos.
    # # JugueteHabitat tiene (id_juguete, id_habitat).
    # relaciones_pendientes = filter(
    #     lambda jh: jh.id_juguete not in juguetes_aparecidos,
    #     generador_juguete_habitat
    # )
    
    # # 3. Obtenemos los id_habitat únicos de esas relaciones pendientes.
    # # Usamos un set por comprensión para evitar duplicados si un hábitat
    # # tiene varios juguetes pendientes.
    # ids_habitats_interes = {jh.id_habitat for jh in relaciones_pendientes}
    
    # # 4. Retornamos los IDs ordenados ascendentemente.
    # yield from sorted(ids_habitats_interes)
    pass


def cadena_creacion(generador_juguete_recurso: Generator, generador_recurso_recurso: Generator,
                    id_recurso: int) -> dict:
    
    lista_jr = list(generador_juguete_recurso)
    lista_rr = list(generador_recurso_recurso)
    
    # 1. Identificar TODOS los recursos que participan en una sola pasada.
    # Como lista_rr viene ordenada de mayor a menor, nunca nos saltaremos una dependencia.
    todos_los_ids = {id_recurso}
    
    for rr in lista_rr:
        if rr.id_recurso in todos_los_ids:
            # Usamos map para extraer solo el id_ingrediente (la posición 0 de la tupla)
            ingredientes = map(lambda tupla_req: tupla_req[0], rr.recursos)
            for ing in ingredientes:
                todos_los_ids.add(ing)

    # 2. Creamos el "esqueleto" de diccionarios aplicando filter y map
    nodos = {}
    for id_res in todos_los_ids:
        # Filtramos los juguetes que producen específicamente este recurso
        juguetes_filtrados = filter(lambda jr: jr.id_recurso == id_res, lista_jr)
        
        # Mapeamos para quedarnos únicamente con los IDs de esos juguetes
        ids_juguetes = tuple(map(lambda jr: jr.id_juguete, juguetes_filtrados))
        
        nodos[id_res] = {"recursos": {}, "juguetes": ids_juguetes}

    # 3. Conectamos los diccionarios (Anidación por referencia)
    # Filtramos la lista de recetas para procesar solo las que nos interesan
    recetas_utiles = filter(lambda rr: rr.id_recurso in todos_los_ids, lista_rr)
    
    for rr in recetas_utiles:
        for id_ingrediente, _ in rr.recursos:
            # Anidamos el diccionario completo del ingrediente
            nodos[rr.id_recurso]["recursos"][id_ingrediente] = nodos[id_ingrediente]

    # 4. Retornamos solo el nivel superior solicitado, como exige el enunciado
    return {id_recurso: nodos[id_recurso]}
    





    # lista_jr = list(generador_juguete_recurso)
    # lista_rr = list(generador_recurso_recurso)
    
    # # 2. Primero identificamos TODOS los recursos que participan en la cadena
    # # Usamos un set para evitar duplicados y ciclos
    # pendientes = [id_recurso]
    # todos_los_ids = set()
    
    # # Buscamos hacia atrás todas las dependencias
    # idx = 0
    # while idx < len(pendientes):
    #     actual = pendientes[idx]
    #     idx += 1
    #     if actual not in todos_los_ids:
    #         todos_los_ids.add(actual)
    #         # Buscamos ingredientes de este recurso en la lista_rr
    #         for rr in lista_rr:
    #             if rr.id_recurso == actual:
    #                 for id_ingrediente, _ in rr.recursos:
    #                     if id_ingrediente not in todos_los_ids:
    #                         pendientes.append(id_ingrediente)
    #                 break

    # # 3. Creamos un "esqueleto" de diccionarios para cada ID encontrado
    # # Esto nos permite tener una referencia para cada nivel
    # nodos = {
    #     id_res: {
    #         "recursos": {}, 
    #         "juguetes": tuple(jr.id_juguete for jr in lista_jr if jr.id_recurso == id_res)
    #     } 
    #     for id_res in todos_los_ids
    # }

    # # 4. Conectamos los diccionarios (Anidación)
    # # Recorremos cada recurso y, si tiene ingredientes, apuntamos a su esqueleto en 'nodos'
    # for id_res in todos_los_ids:
    #     for rr in lista_rr:
    #         if rr.id_recurso == id_res:
    #             for id_ingrediente, _ in rr.recursos:
    #                 # Aquí ocurre la magia: anidamos el diccionario completo del ingrediente
    #                 nodos[id_res]["recursos"][id_ingrediente] = nodos[id_ingrediente]
    #             break

    # # 5. Retornamos solo el nivel superior solicitado
    # return {id_recurso: nodos[id_recurso]}
    pass


def juguetes_a_aparecer(generador_juguete_habitat: Generator, generador_periodo_dia: Generator,
                        id_habitat: int, momento_dia: int = 0) -> Generator:
    periodos = tuple(generador_periodo_dia)
    rangos_periodos = []
    acumulado = 0
    
    for p in periodos:
        horas_str, minutos_str = p.duracion.split(':')
        duracion_mins = (int(horas_str) * 60) + int(minutos_str)
        # Guardamos: (id_periodo, minuto_inicio, minuto_fin)
        rangos_periodos.append((p.id_periodo_dia, acumulado, acumulado + duracion_mins))
        acumulado += duracion_mins
        
    total_dia_mins = acumulado
    juguetes_resultado = []
    
    # 2. Filtrado y cálculo de esperas
    for jh in generador_juguete_habitat:
        if jh.id_habitat == id_habitat:
            horas_esp_str, minutos_esp_str = jh.tiempo_espera.split(':')
            t_base = (int(horas_esp_str) * 60) + int(minutos_esp_str)
            
            minuto_llegada_absoluto = momento_dia + t_base
            minuto_en_dia = minuto_llegada_absoluto % total_dia_mins
            
            # --- APLICACIÓN DEL ESTILO FUNCIONAL ---
            # 1. Filtramos para obtener solo los periodos que el juguete permite
            periodos_validos = filter(lambda rango: rango[0] in jh.ids_periodo_dia, rangos_periodos)
            
            # 2. Mapeamos esos periodos para calcular la distancia en minutos. 
            # Si el minuto actual cae dentro del rango, la espera es 0. 
            # Si no, calculamos la distancia matemática.
            esperas = map(lambda rango: 0 if rango[1] <= minuto_en_dia < rango[2] 
                          else (rango[1] - minuto_en_dia) % total_dia_mins, periodos_validos)
            
            # 3. Extraemos el valor mínimo de nuestro mapeo
            min_espera_extra = min(esperas)
            # ---------------------------------------
            
            t_final = t_base + min_espera_extra
            juguetes_resultado.append((t_final, jh.id_juguete))
            
        elif jh.id_habitat > id_habitat:
            # Mantenemos el break porque los datos están ordenados por id_habitat.
            break

    # 3. Ordenar por orden de aparición y luego por id_juguete
    juguetes_resultado.sort()
    
    # 4. Generar la respuesta final
    for t_final, id_juguete in juguetes_resultado:
        yield (id_juguete, t_final)
    







    # # 1. Procesar los periodos del día
    # # Consumimos el generador a una tupla porque necesitamos iterarlo varias veces 
    # periodos = tuple(generador_periodo_dia)
    # rangos_periodos = []
    # acumulado = 0
    
    # for p in periodos:
    #     horas_str, minutos_str = p.duracion.split(':')
    #     duracion_mins = (int(horas_str) * 60) + int(minutos_str)
    #     # Guardamos: (id_periodo, minuto_inicio, minuto_fin)
    #     rangos_periodos.append((p.id_periodo_dia, acumulado, acumulado + duracion_mins))
    #     acumulado += duracion_mins
        
    # total_dia_mins = acumulado
    
    # # Lista temporal para guardar los juguetes de ESTE hábitat y poder ordenarlos
    # juguetes_resultado = []
    
    # # 2. Filtrado y cálculo de esperas
    # for jh in generador_juguete_habitat:
    #     if jh.id_habitat == id_habitat:
    #         # Calcular tiempo base en minutos
    #         horas_esp_str, minutos_esp_str = jh.tiempo_espera.split(':')
    #         t_base = (int(horas_esp_str) * 60) + int(minutos_esp_str)
            
    #         minuto_llegada_absoluto = momento_dia + t_base
    #         minuto_en_dia = minuto_llegada_absoluto % total_dia_mins
            
    #         min_espera_extra = float('inf')
            
    #         # Buscar el periodo válido más cercano
    #         for id_p, inicio, fin in rangos_periodos:
    #             if id_p in jh.ids_periodo_dia:
    #                 # Si ya estamos dentro del periodo válido, la espera extra es 0
    #                 if inicio <= minuto_en_dia < fin:
    #                     min_espera_extra = 0
    #                     break
    #                 else:
    #                     # Calculamos la distancia hasta el inicio de este periodo válido
    #                     # El módulo asegura que funcione incluso si el periodo es al día siguiente
    #                     distancia = (inicio - minuto_en_dia) % total_dia_mins
    #                     if distancia < min_espera_extra:
    #                         min_espera_extra = distancia
                            
    #         # El tiempo total que tardará en aparecer desde el momento actual
    #         t_final = t_base + min_espera_extra
            
    #         # Guardamos (t_final, id_juguete) para que el ordenamiento nativo actúe en ese orden
    #         juguetes_resultado.append((t_final, jh.id_juguete))
            
    #     elif jh.id_habitat > id_habitat:
    #         # OPTIMIZACIÓN CLAVE: 
    #         # Los datos vienen ordenados por id_habitat. 
    #         # Si encontramos un id_habitat mayor, significa que ya pasamos todos los
    #         # que nos servían. Hacemos 'break' para no seguir leyendo un archivo gigante.
    #         break

    # # 3. Ordenar por orden de aparición y luego por id_juguete (criterio de desempate)
    # juguetes_resultado.sort()
    
    # # 4. Generar la respuesta final
    # for t_final, id_juguete in juguetes_resultado:
    #     yield (id_juguete, t_final)
    pass


def juguetes_autosuficientes(generador_juguete: Generator,
                             generador_juguete_objeto: Generator,
                             generador_objeto_recurso: Generator,
                             generador_juguete_recurso: Generator,
                             generador_recurso_recurso: Generator) -> Generator:
    
    # 1. Cargar datos en diccionarios clásicos
    recurso_natural_por_juguete = {}
    for juguete_recurso in generador_juguete_recurso:
        recurso_natural_por_juguete[juguete_recurso.id_juguete] = juguete_recurso.id_recurso
        
    favoritos_por_juguete = {}
    for juguete_objeto in generador_juguete_objeto:
        if juguete_objeto.id_juguete not in favoritos_por_juguete:
            favoritos_por_juguete[juguete_objeto.id_juguete] = []
        favoritos_por_juguete[juguete_objeto.id_juguete].append(juguete_objeto.id_objeto)
        
    recetas_objetos = {}
    for objeto_recurso in generador_objeto_recurso:
        recursos_necesarios = []
        for id_rec, cantidad in objeto_recurso.recursos:
            recursos_necesarios.append(id_rec)
        recetas_objetos[objeto_recurso.id_objeto] = recursos_necesarios
        
    # Las recetas de recursos vienen de mayor a menor[cite: 141]. 
    # Las guardamos y ordenamos de menor a mayor para resolver dependencias.
    lista_recetas_recursos = []
    for recurso_recurso in generador_recurso_recurso:
        recursos_req = []
        for id_rec, cantidad in recurso_recurso.recursos:
            recursos_req.append(id_rec)
        lista_recetas_recursos.append((recurso_recurso.id_recurso, recurso_recurso.id_afinidad, recursos_req))
    
    lista_recetas_recursos.sort(key=lambda x: x[0])
    
    # 2. Iterar sobre cada juguete para ver si es autosuficiente
    for juguete in generador_juguete:
        id_jug = juguete.id_juguete
        
        # Filtro: si no tiene recurso natural o no tiene favoritos, no puede ser autosuficiente
        if id_jug not in recurso_natural_por_juguete or id_jug not in favoritos_por_juguete:
            continue
            
        afinidades_juguete = set()
        for afinidad in juguete.afinidades:
            afinidades_juguete.add(afinidad)
            
        # Iniciar inventario con su recurso natural
        recurso_base = recurso_natural_por_juguete[id_jug]
        recursos_obtenibles = set()
        recursos_obtenibles.add(recurso_base)
        
        # 3. Intentar descubrir nuevos recursos en cascada
        for id_rec_resultante, id_afinidad_req, reqs in lista_recetas_recursos:
            if id_afinidad_req in afinidades_juguete:
                puede_crear_recurso = True
                for req in reqs:
                    if req not in recursos_obtenibles:
                        puede_crear_recurso = False
                        break
                
                if puede_crear_recurso:
                    recursos_obtenibles.add(id_rec_resultante)
                    
        # 4. Comprobar si puede armar al menos un objeto favorito
        objetos_favoritos = favoritos_por_juguete[id_jug]
        puede_armar_algun_favorito = False
        
        for id_objeto in objetos_favoritos:
            if id_objeto in recetas_objetos:
                recursos_para_objeto = recetas_objetos[id_objeto]
                puede_armar_este_objeto = True
                
                for rec_req in recursos_para_objeto:
                    if rec_req not in recursos_obtenibles:
                        puede_armar_este_objeto = False
                        break
                
                if puede_armar_este_objeto:
                    puede_armar_algun_favorito = True
                    break  # Con uno que pueda armar, ya es suficiente 
                    
        # 5. Entregar el juguete si cumplió las condiciones
        if puede_armar_algun_favorito:
            yield id_jug
    pass


def habitat_eventualmente_creables(generador_juguete: Generator,
                                   generador_juguete_recurso: Generator,
                                   generador_recurso_recurso: Generator,
                                   generador_objeto_recurso: Generator,
                                   generador_habitat_objeto: Generator) -> Generator:
    # 1. Recolectar datos de los juguetes que ya están presentes
    id_juguetes_presentes = set()
    afinidades_presentes = set()
    
    for juguete in generador_juguete:
        id_juguetes_presentes.add(juguete.id_juguete)
        for afinidad in juguete.afinidades:
            afinidades_presentes.add(afinidad)
            
    # 2. Obtener los recursos naturales base de esos juguetes
    recursos_obtenibles = set()
    
    for juguete_recurso in generador_juguete_recurso:
        if juguete_recurso.id_juguete in id_juguetes_presentes:
            recursos_obtenibles.add(juguete_recurso.id_recurso)
            
    # 3. Expandir los recursos obtenibles con las recetas
    # Guardamos en una lista y ordenamos de menor a mayor ID (como exige el enunciado)
    lista_recurso_recurso = list(generador_recurso_recurso)
    lista_recurso_recurso.sort(key=lambda receta: receta.id_recurso)
    
    for receta in lista_recurso_recurso:
        if receta.id_afinidad in afinidades_presentes:
            puede_fabricarse = True
            for id_rec_req, cantidad in receta.recursos:
                if id_rec_req not in recursos_obtenibles:
                    puede_fabricarse = False
                    break
            
            if puede_fabricarse:
                recursos_obtenibles.add(receta.id_recurso)
                
    # 4. Calcular qué objetos se pueden armar con esos recursos
    objetos_fabricables = set()
    
    for objeto_recurso in generador_objeto_recurso:
        puede_fabricarse = True
        for id_rec_req, cantidad in objeto_recurso.recursos:
            if id_rec_req not in recursos_obtenibles:
                puede_fabricarse = False
                break
                
        if puede_fabricarse:
            objetos_fabricables.add(objeto_recurso.id_objeto)
            
    # 5. Finalmente, evaluar qué hábitats se pueden armar con esos objetos
    for habitat_objeto in generador_habitat_objeto:
        puede_fabricarse = True
        for id_obj_req, cantidad in habitat_objeto.objetos:
            if id_obj_req not in objetos_fabricables:
                puede_fabricarse = False
                break
                
        if puede_fabricarse:
            yield habitat_objeto.id_habitat
    pass

def avanzar_produccion(generador_juguete_recurso: Generator,
                       generador_juguete_objeto: Generator,
                       JugueteProductor: NodoLigado | None,
                       objetos: set,
                       minutos: int = 1) -> Generator:
    
    # 1. Cargar datos de producción en un diccionario
    # info_produccion = {id_juguete: (id_recurso, tiempo_espera_mins, cantidad_base)}
    info_produccion = {}
    for jr in generador_juguete_recurso:
        horas_str, minutos_str = jr.tiempo_espera.split(':')
        t_espera_mins = (int(horas_str) * 60) + int(minutos_str)
        info_produccion[jr.id_juguete] = (jr.id_recurso, t_espera_mins, jr.cantidad)
        
    # 2. Cargar objetos favoritos por juguete
    # favoritos_juguete = {id_juguete: [id_objeto1, id_objeto2, ...]}
    favoritos_juguete = {}
    for jo in generador_juguete_objeto:
        if jo.id_juguete not in favoritos_juguete:
            favoritos_juguete[jo.id_juguete] = []
        favoritos_juguete[jo.id_juguete].append(jo.id_objeto)
        
    # 3. Recorrer la cadena de Nodos (Juguetes que están en el refugio)
    recursos_creados = {}
    actual = JugueteProductor
    
    while actual is not None:
        id_jug = actual.id
        
        if id_jug in info_produccion:
            id_rec, t_espera, cant_base = info_produccion[id_jug]
            
            # Calcular bono por favoritos presentes usando programación funcional (filter)
            favoritos_presentes = 0
            if id_jug in favoritos_juguete:
                # Usamos filter para conservar solo los favoritos que existen en el set 'objetos'
                favs_del_juguete = favoritos_juguete[id_jug]
                favs_presentes = list(filter(lambda obj: obj in objetos, favs_del_juguete))
                
                # El enunciado especifica usar la cantidad de favoritos DISTINTOS
                # Pasamos a set para evitar contar duplicados si los hubiera
                favoritos_presentes = len(set(favs_presentes))
                
            # Fórmula de producción con el bono
            cant_final_por_ciclo = int(cant_base * (1 + 0.1 * favoritos_presentes))
            
            # Avanzar el tiempo y calcular ciclos producidos
            tiempo_total = actual.tiempo_actual + minutos
            ciclos = tiempo_total // t_espera
            
            # Actualizamos el estado interno del NodoLigado (el tiempo vuelve a iniciar)
            actual.tiempo_actual = tiempo_total % t_espera
            
            # Si se completó al menos un ciclo, sumamos la producción
            if ciclos > 0:
                produccion_total = ciclos * cant_final_por_ciclo
                
                if id_rec not in recursos_creados:
                    recursos_creados[id_rec] = 0
                recursos_creados[id_rec] += produccion_total
                
        # Avanzar al siguiente nodo de la lista ligada
        actual = actual.siguiente
        
    # 4. Retornar generador ordenado por id_recurso usando map y sorted (tu estilo)
    ids_ordenados = sorted(recursos_creados.keys())
    yield from map(
        lambda id_r: (id_r, recursos_creados[id_r]), 
        ids_ordenados
    )
    pass


def crear_recursos(generador_juguete_recurso: Generator,
                   generador_juguete_objeto: Generator) -> Generator:
    
    # 1. Cargar datos en diccionarios para consultas O(1)
    info_produccion = {}
    for jr in generador_juguete_recurso:
        horas_str, minutos_str = jr.tiempo_espera.split(':')
        t_espera_mins = (int(horas_str) * 60) + int(minutos_str)
        info_produccion[jr.id_juguete] = (jr.id_recurso, t_espera_mins, jr.cantidad)
        
    favoritos_juguete = {}
    for jo in generador_juguete_objeto:
        if jo.id_juguete not in favoritos_juguete:
            favoritos_juguete[jo.id_juguete] = []
        favoritos_juguete[jo.id_juguete].append(jo.id_objeto)
        
    # 2. Variables de estado interno (simulan la memoria del juego)
    cabeza_juguetes = None
    set_objetos = set()
    
    # 3. "Cebar" (Prime) la corrutina. 
    # El primer yield se pausa esperando el comando inicial.
    comando = yield
    
    # 4. Bucle infinito para recibir y procesar comandos de forma dinámica
    while True:
        if comando == "end":
            # Entregar la tupla final y terminar la función por completo
            yield (cabeza_juguetes, set_objetos)
            break
            
        elif comando is None or isinstance(comando, int):
            # Comportamiento: avanzar el tiempo
            minutos = 1 if comando is None else comando
            
            recursos_creados = {}
            actual = cabeza_juguetes
            
            # Reutilizamos la lógica exitosa de avanzar_produccion
            while actual is not None:
                id_jug = actual.id
                
                if id_jug in info_produccion:
                    id_rec, t_espera, cant_base = info_produccion[id_jug]
                    
                    favoritos_presentes = 0
                    if id_jug in favoritos_juguete:
                        favs_del_juguete = favoritos_juguete[id_jug]
                        favs_presentes = list(filter(lambda obj: obj in set_objetos, favs_del_juguete))
                        favoritos_presentes = len(set(favs_presentes))
                        
                    cant_final_por_ciclo = int(cant_base * (1 + 0.1 * favoritos_presentes))
                    
                    tiempo_total = actual.tiempo_actual + minutos
                    ciclos = tiempo_total // t_espera
                    actual.tiempo_actual = tiempo_total % t_espera
                    
                    if ciclos > 0:
                        produccion_total = ciclos * cant_final_por_ciclo
                        if id_rec not in recursos_creados:
                            recursos_creados[id_rec] = 0
                        recursos_creados[id_rec] += produccion_total
                        
                actual = actual.siguiente
                
            # Formatear el resultado en una tupla ordenada a tu estilo funcional
            ids_ordenados = sorted(recursos_creados.keys())
            tupla_resultado = tuple(map(lambda id_r: (id_r, recursos_creados[id_r]), ids_ordenados))
            
            # Entregamos la tupla y esperamos el siguiente comando
            comando = yield tupla_resultado
            
        elif isinstance(comando, set):
            # Comportamiento: Agregar objetos al inventario
            for obj in comando:
                set_objetos.add(obj)
                
            # "No entrega un valor"
            comando = yield None
            
        else:
            # Comportamiento: Si no es None, int, set o "end", es un Juguete.
            # Lo instanciamos en un NodoLigado. Como la clase hereda de NodoLigadoAbstracto, 
            # asume kwargs de tiempo_actual=0.
            nuevo_nodo = NodoLigado(comando.id_juguete, siguiente=None, tiempo_actual=0)
            
            if cabeza_juguetes is None:
                cabeza_juguetes = nuevo_nodo
            else:
                # Utilizamos tu método insertar que desarrollamos al inicio
                cabeza_juguetes = cabeza_juguetes.insertar(nuevo_nodo)
                
            # "No entrega un valor"
            comando = yield None
    pass


def agregar_recursos(recurso: NodoLigado | None, nuevos_recursos: tuple) -> object:
    """
    Agrega nuevos recursos a la cadena de NodoLigado.
    Si el recurso ya existe, suma la cantidad.
    Si no existe, crea un nuevo nodo y lo inserta manteniendo el orden.
    """
    cabeza = recurso
    
    for id_rec, cantidad in nuevos_recursos:
        # 1. Si la cadena está vacía, creamos el primer nodo
        if cabeza is None:
            cabeza = NodoLigado(id_rec, siguiente=None, cantidad=cantidad)
            continue
            
        # 2. Búsqueda manual: recorremos la cadena para ver si el recurso ya existe
        actual = cabeza
        encontrado = False
        
        while actual is not None:
            if actual.id == id_rec:
                # ¡Lo encontramos! Sumamos la cantidad y marcamos la bandera
                actual.cantidad += cantidad
                encontrado = True
                break
            actual = actual.siguiente
            
        # 3. Si terminamos de recorrer y no estaba, lo insertamos manualmente
        if not encontrado:
            nuevo_nodo = NodoLigado(id_rec, siguiente=None, cantidad=cantidad)
            
            # Lógica de inserción manual manteniendo el orden de menor a mayor
            if nuevo_nodo.id < cabeza.id:
                # Caso especial: el nuevo nodo tiene un ID menor que la cabeza actual
                nuevo_nodo.siguiente = cabeza
                cabeza = nuevo_nodo
            else:
                # Recorremos buscando la posición correcta entre los nodos
                actual = cabeza
                while actual.siguiente is not None and actual.siguiente.id < nuevo_nodo.id:
                    actual = actual.siguiente
                    
                # Conectamos el nuevo nodo en medio (o al final) de la cadena
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                
    return cabeza
    pass


def por_aparecer(generador_juguete: Generator, Habitat: NodoLigado | None, generador_juguete_habitat: Generator,
                 generador_periodo_dia: Generator, momento_dia: int = 0) -> Generator:
    # 1. Identificar juguetes que ya están en el refugio
    juguetes_presentes = set(map(lambda j: j.id_juguete, generador_juguete))
    
    # 2. Procesar los periodos del día
    periodos = tuple(generador_periodo_dia)
    rangos_periodos = []
    acumulado = 0
    for p in periodos:
        horas_str, minutos_str = p.duracion.split(':')
        duracion_mins = (int(horas_str) * 60) + int(minutos_str)
        rangos_periodos.append((p.id_periodo_dia, acumulado, acumulado + duracion_mins))
        acumulado += duracion_mins
        
    total_dia_mins = acumulado
    
    # Set para evitar que un juguete gane en dos hábitats a la vez
    juguetes_asignados = set()
    
    # TRUCO EXPERTO DE MEMORIA: Convertimos el generador en un iterador manual
    jh_iterator = iter(generador_juguete_habitat)
    current_jh = next(jh_iterator, None)
    
    # 3. Iterar la lista ligada de Hábitats
    actual = Habitat
    while actual is not None:
        id_hab = actual.id
        tiempo_pres = actual.tiempo_presente
        
        # Avanzamos el iterador del archivo hasta empatar con nuestro Hábitat actual
        while current_jh is not None and current_jh.id_habitat < id_hab:
            current_jh = next(jh_iterator, None)
            
        candidatos_validos = []
        
        # Recolectamos TODAS las reglas que le pertenecen SÓLO a este hábitat
        while current_jh is not None and current_jh.id_habitat == id_hab:
            id_jug = current_jh.id_juguete
            
            if id_jug not in juguetes_presentes:
                horas_esp_str, minutos_esp_str = current_jh.tiempo_espera.split(':')
                t_base = (int(horas_esp_str) * 60) + int(minutos_esp_str)
                
                # Matemática de tiempo: Calculamos el minuto exacto de llegada
                momento_creacion = momento_dia - tiempo_pres
                minuto_base = momento_creacion + t_base
                minuto_base_en_dia = minuto_base % total_dia_mins
                
                periodos_validos = list(filter(lambda rango: rango[0] in current_jh.ids_periodo_dia, rangos_periodos))
                
                if periodos_validos:
                    esperas = map(lambda rango: 0 if rango[1] <= minuto_base_en_dia < rango[2] 
                                  else (rango[1] - minuto_base_en_dia) % total_dia_mins, periodos_validos)
                    
                    min_espera_extra = min(esperas)
                    tiempo_aparicion_final = t_base + min_espera_extra
                    
                    # Filtro: Sólo consideramos a los que NO se han vencido
                    if tiempo_pres <= tiempo_aparicion_final:
                        # Guardamos (tiempo_total_a_esperar, id_juguete)
                        candidatos_validos.append((tiempo_aparicion_final, id_jug))
                        
            # Avanzamos a la siguiente regla
            current_jh = next(jh_iterator, None)
            
        # 4. Decidir al ganador absoluto para este hábitat
        # sort() ordenará por tiempo menor y, en caso de empate, por id_juguete menor
        candidatos_validos.sort()
        ganador = None
        
        for tiempo_llegada, id_candidato in candidatos_validos:
            if id_candidato not in juguetes_asignados:
                ganador = id_candidato
                juguetes_asignados.add(id_candidato)
                break  # Encontramos al campeón, no buscamos más
                
        yield ganador
        actual = actual.siguiente
    pass


def habitat_creables(generador_juguete: Generator, generador_juguete_recurso: Generator,
                     generador_recurso_recurso: Generator, generador_objeto_recurso: Generator,
                     generador_habitat_objeto: Generator, Recurso: NodoLigado | None) -> Generator:
    # 1. Obtener afinidades de los juguetes que YA están en el refugio
    afinidades_presentes = set()
    for juguete in generador_juguete:
        for af in juguete.afinidades:
            afinidades_presentes.add(af)
            
    # Consumimos este generador por seguridad para no dejarlo colgado
    for _ in generador_juguete_recurso:
        pass
        
    # 2. Cargar el inventario ACTUAL en un diccionario modificable
    inventario = {}
    actual = Recurso
    while actual is not None:
        inventario[actual.id] = actual.cantidad
        actual = actual.siguiente
        
    # 3. Mapear los costos de los objetos en un diccionario
    req_objetos = {}
    for obj_rec in generador_objeto_recurso:
        req_objetos[obj_rec.id_objeto] = obj_rec.recursos
        
    # 4. Guardamos las recetas (ya vienen ordenadas de mayor a menor)
    lista_rr = list(generador_recurso_recurso)
    
    # 5. Evaluar cada hábitat en orden secuencial
    for hab_obj in generador_habitat_objeto:
        faltantes = {}
        es_posible = True
        
        # A. Traducir todos los objetos que pide el hábitat a sus recursos básicos
        for id_obj, cant_obj in hab_obj.objetos:
            if id_obj not in req_objetos:
                es_posible = False
                break
                
            for id_rec, cant_rec_por_obj in req_objetos[id_obj]:
                if id_rec not in faltantes:
                    faltantes[id_rec] = 0
                faltantes[id_rec] += cant_obj * cant_rec_por_obj
                
        if not es_posible:
            continue
            
        # B. Resolución Top-Down de recetas
        for receta in lista_rr:
            id_rec_resultante = receta.id_recurso
            
            # Si necesitamos este recurso complejo
            if id_rec_resultante in faltantes:
                cant_necesitada = faltantes[id_rec_resultante]
                cant_en_inventario = inventario.get(id_rec_resultante, 0)
                
                # Y nos falta más de lo que tenemos
                if cant_necesitada > cant_en_inventario:
                    
                    # Verificamos si TENEMOS la afinidad y si la receta ES VÁLIDA (no vacía)
                    if receta.id_afinidad in afinidades_presentes and len(receta.recursos) > 0:
                        cant_a_crear = cant_necesitada - cant_en_inventario
                        
                        # Traspasamos la deuda a los ingredientes menores
                        for id_ing, cant_ing_req in receta.recursos:
                            if id_ing not in faltantes:
                                faltantes[id_ing] = 0
                            faltantes[id_ing] += cant_a_crear * cant_ing_req
                            
                        # Ajustamos la deuda actual a lo que tomaremos del inventario
                        faltantes[id_rec_resultante] = cant_en_inventario
        
        # C. Comprobación final contra el inventario
        for id_rec, cant_final_req in faltantes.items():
            if inventario.get(id_rec, 0) < cant_final_req:
                es_posible = False
                break
                
        # D. Consumo real: Si logramos construirlo, descontamos los recursos
        if es_posible:
            for id_rec, cant_final_req in faltantes.items():
                # Actualizamos el inventario para que el próximo hábitat no pueda
                # usar recursos que ya gastamos en este.
                inventario[id_rec] = inventario.get(id_rec, 0) - cant_final_req
                
            yield hab_obj.id_habitat


def manejo_habitat(gen_juguete: Generator,
                   gen_juguete_habitat: Generator,
                   gen_habitat_objeto: Generator,
                   gen_objeto_recurso: Generator,
                   gen_recurso_recurso: Generator,
                   gen_periodo_dia: Generator,
                   tiempo_inicial: int = 0) -> Generator:
    pass


# Simulación

def simular(generador_juguete: Generator, generador_juguete_habitat: Generator,
            generador_habitat_objeto: Generator, generador_objeto_recurso: Generator,
            generador_recurso_recurso: Generator, generador_juguete_recurso: Generator,
            generador_juguete_objeto: Generator, generador_periodo_dia: Generator) -> Generator:
    pass
