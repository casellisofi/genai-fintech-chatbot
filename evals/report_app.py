import streamlit as st
import json
from collections import Counter
from pathlib import Path
import pandas as pd

LOG_PATH = Path(__file__).parent.parent / "logs" / "output_log.jsonl"

st.set_page_config(page_title="Fintech Bot - Reportes", page_icon="📊")
st.title("📊 Reportes de Interacciones del Asistente Virtual")

if not LOG_PATH.exists():
    st.warning("No se encontraron logs aún.")
else:
    lines = LOG_PATH.read_text(encoding="utf-8").splitlines()
    data = [json.loads(line) for line in lines]

    df = pd.DataFrame(data)
    total = len(df)

    st.subheader("🔢 Totales Generales")
    st.write(f"Total de interacciones: **{total}**")
    st.write(f"Saludos detectados: **{df['greeting_mode'].sum()}** ({df['greeting_mode'].mean():.1%})")
    st.write(f"Uso de base de conocimientos (KB): **{df['used_kb'].sum()}** ({df['used_kb'].mean():.1%})")

    st.subheader("🧩 Distribución por Categoría Detectada")
    if "matched_category" in df.columns:
        st.bar_chart(df["matched_category"].value_counts())

    st.subheader("📄 Últimas Interacciones")
    st.dataframe(df[["timestamp", "user_input", "matched_category", "greeting_mode", "used_kb"]].sort_values(by="timestamp", ascending=False).head(20))
