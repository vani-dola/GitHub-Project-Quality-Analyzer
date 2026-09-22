import ast
def analyze_structure(repository):
    """
    Analyze the complete structure of a GitHub repository recursively.
    """

    files = []
    folders = []

    def scan_folder(path=""):
        contents = repository.get_contents(path, ref=repository.default_branch)

        for item in contents:
            if item.type == "file":
                files.append(item.path)

            elif item.type == "dir":
                folders.append(item.path)
                scan_folder(item.path)

    scan_folder()

    return {
        "files": files,
        "folders": folders
    }
def analyze_code_quality(repository):
    """
    Analyze basic code quality of a GitHub repository recursively.
    """

    python_files = []
    total_lines = 0
    quality_score = 100
    long_files = []
    long_functions = []
    suggestions = []

    def scan_folder(path=""):
        nonlocal total_lines

        contents = repository.get_contents(
            path,
            ref=repository.default_branch
        )

        for item in contents:
            if item.type == "file" and item.name.endswith(".py"):
                python_files.append(item.path)

                try:
                    file_content = repository.get_contents(
                        item.path,
                        ref=repository.default_branch
                    )

                    content = file_content.decoded_content.decode("utf-8")
                    total_lines += len(content.splitlines())

                    line_count = len(content.splitlines())

                    if line_count > 300:
                        long_files.append(item.path)

                    try:
                        tree = ast.parse(content)

                        for node in ast.walk(tree):
                            if isinstance(
                                node,
                                (ast.FunctionDef, ast.AsyncFunctionDef)
                            ):
                                function_length = (
                                    node.end_lineno - node.lineno + 1
                                )

                                if function_length > 50:
                                    long_functions.append(
                                        f"{item.path}:{node.name}"
                                    )

                    except SyntaxError:
                        pass

                except Exception:
                    pass

            elif item.type == "dir":
                scan_folder(item.path)

    scan_folder()

    if len(python_files) == 0:
        quality_score -= 20
        suggestions.append("No Python files found.")

    if len(python_files) > 10:
        suggestions.append(
            "Consider organizing Python files into folders."
        )

    if long_files:
        quality_score -= 10
        suggestions.append(
            f"Long Python files found: {long_files}"
        )

    if long_functions:
        quality_score -= 10
        suggestions.append(
            f"Long functions found: {long_functions}"
        )

    if quality_score < 0:
        quality_score = 0

    return {
        "score": quality_score,
        "python_files": python_files,
        "total_lines": total_lines,
        "suggestions": suggestions
    }



def analyze_readme(repository):
    """
    Analyze the README file of a GitHub repository.
    """

    try:
        readme = repository.get_readme()
        content = readme.decoded_content.decode("utf-8")

        score = 100
        suggestions = []

        required_sections = [
            "installation",
            "usage",
            "features",
            "license"
        ]

        for section in required_sections:
            if section not in content.lower():
                score -= 10
                suggestions.append(
                    f"{section.capitalize()} section is missing."
                )

        if not content.strip().startswith("#"):
            score -= 10
            suggestions.append("README title is missing.")

        if len(content.strip()) < 200:
            score -= 30
            suggestions.append("README.md is too short.")

    
        if score < 0:
            score = 0

        return {
            "score": score,
            "suggestions": suggestions
        }

    except Exception:
        return {
            "score": 0,
            "suggestions": ["README.md could not be analyzed."]
        }

def analyze_security(repository):
    """
    Perform basic security checks on a GitHub repository.
    """

    security_score = 100
    findings = []

    sensitive_names = [
        ".env",
        "credentials.json",
        "secrets.json"
    ]

    secret_keywords = [
        "api_key",
        "apikey",
        "secret_key",
        "password",
        "access_token",
        "auth_token"
    ]

    def scan_folder(path=""):
        nonlocal security_score

        contents = repository.get_contents(
            path,
            ref=repository.default_branch
        )

        for item in contents:
            if item.type == "file":

                if item.name.lower() in sensitive_names:
                    security_score -= 30
                    findings.append(
                        f"Sensitive file found: {item.path}"
                    )

                if item.name.endswith((".py", ".js", ".java", ".json", ".txt")):
                    try:
                        file_content = repository.get_contents(
                            item.path,
                            ref=repository.default_branch
                        )

                        content = file_content.decoded_content.decode(
                            "utf-8",
                            errors="ignore"
                        )

                        content_lower = content.lower()

                        for keyword in secret_keywords:
                            if keyword in content_lower:
                                security_score -= 10
                                findings.append(
                                    f"Possible secret keyword found in: {item.path}"
                                )
                                break

                    except Exception:
                        pass

            elif item.type == "dir":
                scan_folder(item.path)

    scan_folder()

    if security_score < 0:
        security_score = 0

    return {
        "score": security_score,
        "findings": findings
    }


def calculate_overall_score(readme, quality, security):
    """
    Calculate the overall quality score of the repository.
    """

    overall_score = (
        readme["score"] * 0.30
        + quality["score"] * 0.40
        + security["score"] * 0.30
    )

    return round(overall_score)