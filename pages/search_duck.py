from duckduckgo_search import DDGS

def obtener_sitio_web(empresa):
    """
    Obtiene el sitio web de una empresa utilizando DuckDuckGo.

    Args:
        empresa (str): Nombre o razón social de la empresa.

    Returns:
        None: Imprime todos los enlaces encontrados en la búsqueda.
    """
    # Crear una instancia de DDGS
    ddgs = DDGS()

    # Realizar búsqueda de la empresa en DuckDuckGo
    resultados = ddgs.text(f"sitio oficial {empresa}", max_results=3)
    
    # Verificar si hay resultados
    if resultados:
        print(f"Resultados para {empresa}:")
        for i, resultado in enumerate(resultados):
            print(f"{i+1}. {resultado['href']}")
    else:
        print(f"No se encontraron resultados para {empresa}.")

# Ejemplo de uso
empresa = "ABGAM, S.A."
obtener_sitio_web(empresa)

