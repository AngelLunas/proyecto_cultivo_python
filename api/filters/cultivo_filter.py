from typing import Mapping, Any, Callable, Optional, Dict
import unicodedata
import re

def normalize_text(text: Optional[str]) -> str:
    if text is None:
        return ""
    value = unicodedata.normalize("NFKD", str(text))
    value = "".join(character for character in value if not unicodedata.combining(character))
    value = " ".join(value.lower().split())
    return value

def build_row_filter(
    department: Optional[str] = None,
    municipality: Optional[str] = None,
    crop: Optional[str] = None,
) -> Callable[[Mapping[str, Any]], bool]:
    targets_by_field: Dict[str, Optional[str]] = {
        "departamento": normalize_text(department) if department else None,
        "municipio":    normalize_text(municipality) if municipality else None,
        "cultivo":      normalize_text(crop) if crop else None,
    }

    def row_filter(record: Mapping[str, Any]) -> bool:
        return all(
            target is None or target in normalize_text(record.get(field_name))
            for field_name, target in targets_by_field.items()
        )

    return row_filter
