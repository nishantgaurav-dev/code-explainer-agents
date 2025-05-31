import ast
from pathlib import Path
from core.ast_utils import extract_ast_info
from agents.base import BaseAgent

class ParserAgent(BaseAgent):
    def run(self, repo_path: str):
        result = {}
        py_files = Path(repo_path).rglob("*.py")
        for f in py_files:
            result[str(f)] = extract_ast_info(f)
        self.context["ast"] = result
        return result
