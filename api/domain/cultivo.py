from dataclasses import dataclass
from typing import Mapping, Any, Type

@dataclass(frozen=True)
class Cultivo:
    departamento: str
    municipio: str
    cultivo: str

    @classmethod
    def from_record(CultivoClass: Type["Cultivo"], record: Mapping[str, Any]) -> "Cultivo":
        return CultivoClass(
            departamento=str(record.get("departamento", "")).strip(),
            municipio=str(record.get("municipio", "")).strip(),
            cultivo=str(record.get("cultivo", "")).strip(),
        )
