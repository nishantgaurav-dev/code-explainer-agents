from agents.parser_agent import ParserAgent
from agents.doc_generator_agent import DocGeneratorAgent

def main():
    context = {"repo_path": "./sample_project"}

    print("🔍 Running ParserAgent...")
    parser = ParserAgent("Parser", context)
    parser.run(context["repo_path"])

    print("📄 Running DocGeneratorAgent...")
    doc_agent = DocGeneratorAgent("DocGen", context)
    doc_agent.run()

    print("✅ Done. Check context['ast'] for results.")

if __name__ == "__main__":
    main()
