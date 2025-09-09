from pathlib import Path
from typing import List, Mapping, Any, Iterable

from api.excel_stream_reader import ExcelStreamReader
from api.filters.cultivo_filter import build_row_filter
from api.stats.edaphic_statistics import compute_edaphic_medians
from api.config.canonical_names import (
    CANONICAL_NAMES,
    TABLE_FIELD_NAMES,
    NUMERIC_FIELD_NAMES_FOR_MEDIAN,
    MEDIAN_LABELS,
    TABLE_HEADERS,
)
from ui import ask_filters_and_limit, print_progress, finish_progress, print_table_with_medians
from api.config.paths import ensure_excel_exists 

if __name__ == "__main__":
    user_department, user_municipality, user_crop, record_limit = ask_filters_and_limit()

    excel_file_path = ensure_excel_exists()

    row_filter = build_row_filter(
        department=user_department,
        municipality=user_municipality,
        crop=user_crop,
    )

    reader = ExcelStreamReader(path=excel_file_path, sheet=0)
    record_iterator: Iterable[Mapping[str, Any]] = reader.iterate_records(
        canonical_names=CANONICAL_NAMES,
        row_filter=row_filter,
        max_records=record_limit,
    )

    limited_records: List[Mapping[str, Any]] = []
    rows_to_show: List[List[str]] = []
    progress_step = 50

    for record in record_iterator:
        limited_records.append(record)
        rows_to_show.append([str(record.get(key, "") or "") for key in TABLE_FIELD_NAMES])
        if len(limited_records) % progress_step == 0:
            print_progress("Cargando", len(limited_records))
    print_progress("Cargando", len(limited_records))
    finish_progress()

    medians_by_field = compute_edaphic_medians(limited_records, NUMERIC_FIELD_NAMES_FOR_MEDIAN)
    print_table_with_medians(
        base_headers=TABLE_HEADERS,
        rows=rows_to_show,
        medians_by_field=medians_by_field,
        numeric_field_names_in_order=NUMERIC_FIELD_NAMES_FOR_MEDIAN,
        median_labels=MEDIAN_LABELS,
        rows_obtained_count=len(limited_records),
    )
