# -----------------------------------------------------------------------------------
# PROMPT BUILDER MODULE
# -----------------------------------------------------------------------------------
# Construcción del prompt dinámico a partir de rol, ejemplos y contexto.
# -----------------------------------------------------------------------------------

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def build_prompt(system_instruction: str, kb_context: str, examples: list, eval_mode: bool = True):
    reasoning_template = "Razonamiento Interno:\n{thoughts}\n\nRespuesta Final:\n{final_answer}"
    messages = [("system", f"{system_instruction}\n\n{kb_context}" if kb_context else system_instruction)]
    
    for example in examples:
        messages.append(("human", example["user"]))
        if eval_mode and example["assistant"].get("thoughts"):
            messages.append(("ai", reasoning_template.format(**example["assistant"])))
        else:
            messages.append(("ai", example["assistant"]["final_answer"]))
    
    messages.append(MessagesPlaceholder(variable_name="history"))
    messages.append(("human", "{input}"))
    return ChatPromptTemplate.from_messages(messages)

def build_greeting_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente virtual especializado en productos financieros (tarjetas de débito, crédito y préstamos). Responde con amabilidad y brevedad a los saludos generales."),
        ("human", "Hola"),
        ("ai", "¡Hola! ¿En qué puedo ayudarte hoy? Podés preguntarme sobre tarjetas de débito, crédito o préstamos."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
