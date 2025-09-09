from typing import List, Dict, Optional

def ask_optional_text(label: str) -> Optional[str]:
    """
    Pide texto (puede quedar vacío). No se menciona que sea opcional.
    """
    try:
        value = input(f"{label}: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return None
    return value or None

def ask_positive_integer(label: str) -> int:
    """
    Pide un entero positivo (obligatorio). Repite hasta que sea válido.
    """
    while True:
        try:
            raw = input(f"{label}: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            continue
        try:
            number = int(raw)
            if number > 0:
                return number
        except ValueError:
            pass
        print("Por favor escribe un número entero positivo.")

def ask_filters_and_limit() -> tuple[Optional[str], Optional[str], Optional[str], int]:
    department = ask_optional_text("Departamento")
    municipality = ask_optional_text("Municipio")
    crop = ask_optional_text("Cultivo")
    limit = ask_positive_integer("Número de registros a consultar")
    return department, municipality, crop, limit

def print_progress(prefix_text: str, count: int) -> None:
    print(f"\r{prefix_text}... {count} filas leídas", end="", flush=True)

def finish_progress() -> None:
    print()


def _format_median(value: Optional[float]) -> str:
    return f"{value:.2f}" if value is not None else "No disponible"

def print_table_with_medians(
    base_headers: List[str],
    rows: List[List[str]],
    medians_by_field: Dict[str, Optional[float]],
    numeric_field_names_in_order: List[str],
    median_labels: Dict[str, str],
    rows_obtained_count: int,
) -> None:
    median_headers = [f"Mediana {median_labels.get(name, name)}" for name in numeric_field_names_in_order]
    all_headers = base_headers + median_headers

    column_widths = [len(h) for h in all_headers]

    for row in rows:
        extended_row = row + [""] * len(median_headers)
        for i, cell in enumerate(extended_row):
            column_widths[i] = max(column_widths[i], len(cell))

    median_values = [_format_median(medians_by_field.get(name)) for name in numeric_field_names_in_order]
    summary_left = [f"Medianas (sobre {rows_obtained_count} filas obtenidas)"] + [""] * (len(base_headers) - 1)
    summary_row = summary_left + median_values

    for i, cell in enumerate(summary_row):
        column_widths[i] = max(column_widths[i], len(cell))

    row_format = " | ".join("{:<" + str(w) + "}" for w in column_widths)
    separator = "-+-".join("-" * w for w in column_widths)

    print(row_format.format(*all_headers))
    print(separator)
    for row in rows:
        extended = row + [""] * len(median_headers)
        print(row_format.format(*extended))
    print(separator)
    print(row_format.format(*summary_row))
    print()
