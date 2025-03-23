from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def build_prompt(system_instruction: str, kb_context: str, examples: list):
    messages = [("system", f"{system_instruction}\n\n{kb_context}" if kb_context else system_instruction)]
    for example in examples:
        messages.append(("human", example["user"]))
        messages.append(("ai", example["assistant"]))
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
