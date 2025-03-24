# 🤖 Fintech Assistant - Demo Conversacional (FinBot)

Asistente virtual para una fintech utilizando modelos de lenguaje (LLM) con **LangChain**, **Ollama**, y una interfaz en **Streamlit**.

El asistente está diseñado para responder con claridad, precisión y empatía sobre productos financieros: **tarjetas de débito**, **tarjetas de crédito** y **préstamos**, aplicando técnicas avanzadas como **prompt engineering** y **chain-of-thought reasoning**.

---

## Tecnologías utilizadas

- [LangChain](https://www.langchain.com/) - Orquestación de LLMs
- [Ollama](https://ollama.com/) - Modelos locales (ej: Mistral, Llama)
- [Streamlit](https://streamlit.io/) - Interfaz de usuario rápida
- Python 3.11+

---

## Ejecución local

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Instalar y ejecutar el modelo con Ollama

Para correr modelos localmente (como Mistral), este proyecto utiliza **[Ollama](https://ollama.com/)**, una plataforma que permite descargar y ejecutar LLMs en tu máquina sin depender de la nube.

#### ➤ Instalación de Ollama

Según tu sistema operativo:

- **macOS**:
  ```bash
  brew install ollama
  ```
- **Windows**:
  - Descargá el instalador desde: https://ollama.com/download
  - Ejecutalo y seguí las instrucciones.
- **Linux (Debian/Ubuntu)**:
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

Verificá que esté instalado correctamente:

```bash
ollama --version
```

#### ➤ Descargar y correr el modelo Mistral

Una vez instalado Ollama, ejecutá:

```bash
ollama run mistral
```

Esto descargará automáticamente el modelo **Mistral** si es la primera vez que lo usás.

---

### 3. Iniciar la aplicación

```bash
streamlit run core/api/main.py
```

La app se abrirá automáticamente en tu navegador en `http://localhost:8501`.

---

## Funcionalidades principales

- Prompt dinámico basado en rol, ejemplos y razonamiento
- Evaluación con modo razonamiento interno (CoT)
- Clasificación automática de consultas por producto
- Uso de conocimiento estructurado (JSON)
- Modular y preparado para escalar con RAG o agentes

---

## Modo evaluación

Podés ejecutar el asistente en modo evaluación para obtener reasoning + respuesta final usando:

```python
eval_mode=True  # en el build_prompt()
```

---

## Evaluación

El proyecto incluye:
- Métricas automáticas vía logging
- Checklist manual de calidad
- Tests adversariales para alineamiento ético

Más detalles en [`docs/evaluation_strategy.md`](docs/evaluation_strategy.md)