class BaseAgent:
    def __init__(self, name, context):
        self.name = name
        self.context = context  # Shared dict: {"repo_path": ..., "ast": ..., etc.}

    def run(self, **kwargs):
        raise NotImplementedError("Each agent must implement the run() method.")
