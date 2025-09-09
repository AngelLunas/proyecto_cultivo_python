# Proyecto

Aplicación de consola que:
- Lee un archivo **Excel** en *streaming* (sin cargar todo a memoria).
- Pide al usuario: **Departamento → Municipio → Cultivo → Cantidad de registros**.
- Aplica el filtro durante la lectura y **corta** al alcanzar el límite.
- Muestra una **tabla** con: Departamento, Municipio, Cultivo, Topología.
- Calcula las **medianas** de **pH**, **Fósforo (P)** y **Potasio (K)** sobre **las filas realmente obtenidas** y las imprime en una fila de resumen.
- Tolera **tildes, mayúsculas y espacios** en entradas y encabezados.

---

## Requisitos

- Python **3.10+**
- Dependencias en `requirements.txt` (ver más abajo).
- Un archivo Excel con encabezados razonables. El lector busca columnas por **palabra clave** (p. ej. `zinc`, `fosforo`, `potasio`, `ph`) incluso si el encabezado real es largo, como “Zinc (Zn) disponible Olsen mg/kg”.

---

## Estructura del proyecto


- **`api/config/paths.py`**: centraliza la **ruta del Excel** (`ensure_excel_exists()`).
- **`api/config/canonical_names.py`**: define los **campos canónicos** para la tabla y las medianas.
- **`api/ui/console.py`**: pide inputs, muestra progreso y renderiza la tabla + fila de medianas.
- **`api/excel_stream_reader.py`**: lectura en *streaming* con **filtro** y **límite**.

---

## Instalación

```bash
# 1) Crear y activar el entorno virtual
python -m venv .venv
# macOS / Linux:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

# 2) Instalar dependencias
pip install -r requirements.txt


