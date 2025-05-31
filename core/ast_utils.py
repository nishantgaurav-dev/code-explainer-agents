import ast

def extract_ast_info(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    output = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            output.append({
                "type": type(node).__name__,
                "name": node.name,
                "lineno": node.lineno,
                "docstring": ast.get_docstring(node),
            })
    return output
