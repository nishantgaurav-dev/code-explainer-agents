## code-explainer-agents

### Folder structure
```
code-explainer-agents/
├── agents/
│   ├── __init__.py
│   ├── base.py                 # BaseAgent class and shared logic
│   ├── parser_agent.py         # M1: ParserAgent (AST-based)
│   ├── doc_generator_agent.py  # M3: Docstring generator
│   └── router_agent.py         # M10 (lite): Controls flow
│
├── llm/
│   ├── __init__.py
│   ├── local_model.py          # CodeLLaMA / Mistral via Ollama
│   └── prompts.py              # Prompt templates
│
├── core/
│   ├── __init__.py
│   ├── repo_utils.py           # File walking, Git tools
│   └── ast_utils.py            # AST parsing helpers
│
├── configs/
│   └── settings.yaml           # Model settings, agent configs
│
├── cli.py                      # CLI entry point (Click / argparse)
├── main.py                     # Entrypoint to trigger agents
├── requirements.txt
├── README.md
└── .env                        # Optional: model paths, keys
```