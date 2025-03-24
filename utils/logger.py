# -----------------------------------------------------------------------------------
# LOGGER MODULE
# -----------------------------------------------------------------------------------
# Registro estructurado de las interacciones del asistente para métricas y evaluación.
# -----------------------------------------------------------------------------------

import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).parent.parent / "logs" / "output_log.jsonl"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def log_interaction(user_input: str, response: str, matched_category: str = None, used_kb: bool = False, greeting_mode: bool = False):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_input": user_input,
        "response": response,
        "matched_category": matched_category,
        "used_kb": used_kb,
        "greeting_mode": greeting_mode
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
