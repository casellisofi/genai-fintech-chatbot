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
st.title("🤖 Asistente Virtual de Fintech")

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
        if not eval_mode:
            examples = [ex for ex in examples if "🤔" not in ex["assistant"]]
        prompt = build_prompt(prompt_data["system"], f"Base de conocimientos:\n{context}" if context else "", examples)

    chain = get_chain(prompt)
    st.session_state.history.append(HumanMessage(content=user_input))
    response = chain.invoke({"input": user_input, "history": st.session_state.history})
    st.session_state.history.append(AIMessage(content=response.content))

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
    else:
        with st.chat_message("FintechBot"):
            st.write(msg.content)
