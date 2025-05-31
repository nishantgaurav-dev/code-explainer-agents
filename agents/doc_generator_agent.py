from agents.base import BaseAgent
from llm.local_model import generate_docstring

class DocGeneratorAgent(BaseAgent):
    def run(self):
        ast_index = self.context.get("ast", {})
        for file_path, nodes in ast_index.items():
            for node in nodes:
                if not node.get("docstring"):
                    prompt = f"Explain what this {node['type']} `{node['name']}` does."
                    doc = generate_docstring(prompt)
                    node["generated_docstring"] = doc
        return ast_index
