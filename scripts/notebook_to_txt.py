import nbformat
from pathlib import Path
import sys

def extraer_codigo_de_notebook(path_notebook: Path) -> str:
    """
    Extrae el código Python de un notebook .ipynb.

    Args:
        path_notebook: La ruta al archivo de notebook como un objeto Path.

    Returns:
        Una cadena con todo el código extraído o una cadena vacía si ocurre un error.
    """
    try:
        with path_notebook.open('r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        codigo = []
        for cell in nb.cells:
            if cell.get('cell_type') == 'code':
                contenido = cell.get('source', '').strip()
                if contenido:
                    codigo.append(contenido)
        return '\n\n'.join(codigo)

    except FileNotFoundError:
        print(f"Error: El archivo no se encontró en la ruta: {path_notebook}", file=sys.stderr)
        return ""
    except Exception as e:
        print(f"Error al leer o procesar {path_notebook.name}: {e}", file=sys.stderr)
        return ""

def procesar_carpeta(carpeta_notebooks: Path, path_salida: Path, recursivo: bool = True):
    """
    Busca notebooks en una carpeta, extrae su código y lo guarda en un archivo de texto.

    Args:
        carpeta_notebooks: Ruta a la carpeta que contiene los notebooks.
        path_salida: Ruta del archivo de texto donde se guardará el código.
        recursivo: Si es True, busca en subcarpetas.
    """
    if not carpeta_notebooks.is_dir():
        print(f"Error: La carpeta objetivo no existe o no es un directorio: {carpeta_notebooks}", file=sys.stderr)
        return

    # Asegurarse de que el directorio de salida exista
    path_salida.parent.mkdir(parents=True, exist_ok=True)
    
    # Determinar el patrón de búsqueda
    patron_busqueda = '*.ipynb'
    notebooks_iterator = carpeta_notebooks.rglob(patron_busqueda) if recursivo else carpeta_notebooks.glob(patron_busqueda)
    
    encontrados = 0
    with path_salida.open('w', encoding='utf-8') as archivo_salida:
        for path_notebook in notebooks_iterator:
            print(f"Procesando: {path_notebook.relative_to(path_salida.parent)}")
            codigo = extraer_codigo_de_notebook(path_notebook)
            if codigo:
                archivo_salida.write(f"# --- Código extraído de: {path_notebook.name} ---\n")
                archivo_salida.write(codigo + '\n\n')
                encontrados += 1
    
    print(f"\nProceso completado.")
    print(f"Se procesaron {encontrados} notebooks.")
    print(f"El código fue guardado en: {path_salida}")

# === Lógica de Ejecución Robusta ===
if __name__ == '__main__':
    # 1. Determinar la ruta absoluta del script actual
    # Path(__file__) es la ruta del script que se está ejecutando.
    # .resolve() la convierte en una ruta absoluta (ej: C:\proyecto\scripts\mi_script.py)
    path_script_actual = Path(__file__).resolve()

    # 2. Definir la raíz del proyecto
    # Suponiendo que este script está en una carpeta 'scripts', la raíz del proyecto es el directorio padre.
    # (ej: C:\proyecto\scripts\ -> .parent -> C:\proyecto\)
    path_raiz_proyecto = path_script_actual.parent.parent 

    # 3. Construir rutas absolutas para las carpetas de entrada y salida
    # Usamos el operador '/' de pathlib que une rutas de forma segura en cualquier sistema operativo.
    carpeta_objetivo = path_raiz_proyecto / 'notebooks'
    archivo_salida = path_raiz_proyecto / 'codigo_extraido.txt'

    # 4. Ejecutar la función principal con las rutas absolutas y seguras
    procesar_carpeta(carpeta_objetivo, archivo_salida, recursivo=True)