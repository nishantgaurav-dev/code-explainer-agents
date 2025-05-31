# Uses Ollama CLI
import subprocess

def generate_docstring(prompt: str):
    cmd = ["ollama", "run", "codellama", prompt]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()
