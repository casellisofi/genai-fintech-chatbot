# 🤖 Fintech Assistant Demo

Este proyecto muestra cómo usar LangChain + Ollama + Streamlit para construir un asistente virtual para una fintech.

## 🚀 Cómo correr

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Correr modelo local (Ollama):
```bash
ollama run mistral
```

3. Ejecutar la app:
```bash
streamlit run core/api/main.py
```

## 📁 Estructura
- `app/main.py`: App principal con Streamlit
- `config/prompt.json`: Prompt separado en archivo externo
- `requirements.txt`: Dependencias
- `.gitignore`: Archivos ignorados por git
