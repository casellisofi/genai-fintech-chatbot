# -----------------------------------------------------------------------------------
# MAIN MODULE
# -----------------------------------------------------------------------------------
# Interfaz de usuario con Streamlit para el asistente de atención al cliente de fintech.
# -----------------------------------------------------------------------------------

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from utils.json_loader import load_json
from utils.logger import log_interaction
from core.knowledge import KnowledgeBase
from core.classifier import is_greeting, is_farewell, classify_category
from core.prompt_builder import build_prompt, build_greeting_prompt
from core.chat_engine import get_chain

# ------------------ Setup ------------------
base_path = Path(__file__).parent.parent
prompt_data = load_json(base_path / "core" / "prompt" / "prompt.json")
kb = KnowledgeBase(base_path / "core" / "kb" / "knowledge.json")

# ------------------ Interfaz ------------------
st.set_page_config(page_title="Fintech Bot", page_icon="🤖")
eval_mode = st.sidebar.checkbox("🔍 Modo evaluación (mostrar razonamiento interno)", value=False)
st.title("🤖 FinBot - Tu asistente virtual")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Escribí tu consulta...")

if user_input:
    if is_farewell(user_input):
        st.session_state.history.append(HumanMessage(content=user_input))
        st.session_state.history.append(AIMessage(content="¡Hasta luego! Si necesitás ayuda en otro momento, estaré acá para asistirte."))
        st.stop()

    if is_greeting(user_input):
        prompt = build_greeting_prompt()
    else:
        context = kb.get_context_by_input(user_input)
        examples = prompt_data["examples"]
        prompt = build_prompt(prompt_data["system"], f"Base de conocimientos:\n{context}" if context else "", examples, eval_mode=eval_mode)

    chain = get_chain(prompt)
    st.session_state.history.append(HumanMessage(content=user_input))
    response = chain.invoke({"input": user_input, "history": st.session_state.history})

    # Separar razonamiento si eval_mode está activado
    if eval_mode and "Respuesta Final:" in response.content:
        parts = response.content.split("Respuesta Final:")
        thoughts = parts[0].replace("Razonamiento Interno:", "").strip()
        final_response = parts[1].strip()
        st.session_state.history.append(AIMessage(content=final_response))
        with st.chat_message("FintechBot"):
            st.markdown(f"""
**Razonamiento interno:**
```
{thoughts}
```

**Respuesta:** {final_response}
""")
    else:
        st.session_state.history.append(AIMessage(content=response.content))
        with st.chat_message("FintechBot"):
            st.write(response.content)

    log_interaction(
        user_input=user_input,
        response=response.content,
        matched_category=classify_category(user_input),
        used_kb=(not is_greeting(user_input)),
        greeting_mode=is_greeting(user_input)
    )

for msg in st.session_state.history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("Usuario"):
            st.write(msg.content)
    elif not eval_mode:
        with st.chat_message("FintechBot"):
            st.write(msg.content)