from typing import Mapping, Any, Iterable, Optional, Dict, List, Sequence

def median(values: List[float]) -> Optional[float]:
    if not values:
        return None
    ordered_values = sorted(values)
    total_count = len(ordered_values)
    middle_index = total_count // 2
    return (
        ordered_values[middle_index]
        if total_count % 2 == 1
        else (ordered_values[middle_index - 1] + ordered_values[middle_index]) / 2
    )

def compute_edaphic_medians(
    records: Iterable[Mapping[str, Any]],
    numeric_field_names: Sequence[str],
) -> Dict[str, Optional[float]]:
    numeric_values_by_field: Dict[str, List[float]] = {name: [] for name in numeric_field_names}

    for record in records:
        for field_name in numeric_field_names:
            value = record.get(field_name)
            try:
                numeric_values_by_field[field_name].append(float(value))
            except (TypeError, ValueError):
                pass

    return {field_name: median(values) for field_name, values in numeric_values_by_field.items()}
