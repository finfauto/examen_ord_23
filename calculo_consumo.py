def obtener_consumo_por_kilometro(modo_motor: int) -> float:
    """
    El resultado será un decimal con la cantidad de combustible consumida por kilómetro. El resultado usará el litro como unidad de medida

    :param modo_motor:
    :return:
    """
    assert 0 <= modo_motor <= 3, "El modo motor debe estar entre 0 y 3"    # no tocar: no permite modos de motor inválidos
    # realizar la función completa desde aquí


def obtener_consumo_sector(longitud_sector: int, modo_motor: int) -> float:
    """
    Obtener la cantidad de combustible consumido en un sector según modo motor.

    Nota: Se considera que el modo motor es el mismo durante el transcurso de todo el sector

    Importante: La longitud del sector viene expresada en metros.

    :param longitud_sector:
    :param modo_motor:
    :return:
    """
    assert longitud_sector >= 0, "Longitud de sector inválido"  # no tocar: no permite sectores con longitud negativa
    # realizar la función completa desde aquí


def obtener_consumo_vuelta(sectores_vuelta: [{}]) -> float:
    """
    Obtener la cantidad de combustible consumida durante una vuelta. La vuelta viene representada por el parámetro sectores_vuelta, que es una lista en la que
    cada elemento es un diccionario con información del sector

    :param sectores_vuelta:
    :return:
    """
    # realidad la función completa desde aquí
