from utils.json_loader import load_json
from pathlib import Path

class KnowledgeBase:
    def __init__(self, kb_path: Path):
        self.data = load_json(kb_path)

    def get_context_by_input(self, user_input: str) -> str:
        user_input_lower = user_input.lower()
        if "débito" in user_input_lower or "debito" in user_input_lower:
            target = "tarjeta_debito"
        elif "crédito" in user_input_lower or "credito" in user_input_lower:
            target = "tarjeta_credito"
        elif "préstamo" in user_input_lower or "prestamo" in user_input_lower:
            target = "prestamos"
        else:
            return ""

        if target not in self.data:
            return ""

        resumen = [f"Información sobre {target.replace('_', ' ')}:"]
        for subkey, value in self.data[target].items():
            if isinstance(value, list):
                resumen.append(f"  - {subkey}: {', '.join(value)}")
            else:
                resumen.append(f"  - {subkey}: {value}")
        return "\n".join(resumen)
