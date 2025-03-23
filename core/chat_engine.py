from utils.llm_loader import ModelLoader
llm = ModelLoader().load()

def get_chain(prompt_template):
    return prompt_template | llm
