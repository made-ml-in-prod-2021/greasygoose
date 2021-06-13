from dataclasses import dataclass, field
from typing import Dict

@dataclass()
class TrainingParams:
    model_type: str
    model_params: Dict[str, int]
    random_state: int = field(default=42)
