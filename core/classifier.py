# -----------------------------------------------------------------------------------
# CLASSIFIER MODULE
# -----------------------------------------------------------------------------------
# Clasificador básico para identificar si un mensaje es saludo, despedida o categoría temática.
# -----------------------------------------------------------------------------------


def is_greeting(text: str) -> bool:
    greetings = ["hola", "buenas", "buenos días", "buenas tardes", "buenas noches", "hola como estas"]
    return text.strip().lower() in greetings


def is_farewell(text: str) -> bool:
    farewells = ["chau", "chao", "nos vemos", "hasta luego", "adiós", "me voy", "gracias, chau", "ok, chau"]
    return text.strip().lower() in farewells

def classify_category(text: str) -> str:
    text = text.lower()
    if "débito" in text or "debito" in text:
        return "tarjeta_debito"
    elif "crédito" in text or "credito" in text:
        return "tarjeta_credito"
    elif "préstamo" in text or "prestamo" in text:
        return "prestamos"
    elif is_greeting(text):
        return "saludo"
    return "otro"