from langchain_ollama import ChatOllama

class ModelLoader:
    def __init__(self, model_name: str = "mistral"):
        self.model_name = model_name

    def load(self):
        return ChatOllama(model=self.model_name)
