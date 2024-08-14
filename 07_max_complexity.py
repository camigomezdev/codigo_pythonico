"""
Análisis de Complejidad
La complejidad ciclomática de esta función es de 7, calculada de la siguiente manera:

El primer if not data: agrega 1.
El for item in data: no agrega complejidad ciclomática, ya que no es una bifurcación.  
El if isinstance(item, int): agrega 1.
El if item % 2 == 0: agrega 1.
El else asociado al if item % 2 == 0: agrega 1.
El elif isinstance(item, str): agrega 1.
El if item.isnumeric(): agrega 1.
El else asociado al if item.isnumeric(): agrega 1.
"""  # noqa: E501


def process_data(data):
    if not data:
        return None

    result = []
    for item in data:
        if isinstance(item, int):
            if item % 2 == 0:
                result.append(item * 2)
            else:
                result.append(item * 3)
        elif isinstance(item, str):
            if item.isnumeric():
                result.append(int(item) * 4)
            else:
                result.append(item.upper())
        else:
            result.append(None)

    if len(result) > 10:
        result = result[:10]

    return result
