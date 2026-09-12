def analyze_structure(repository):
    """
    Analyze the basic structure of a GitHub repository.
    """

    contents = repository.get_contents("", ref="main")

    files = []
    folders = []

    for item in contents:
        if item.type == "file":
            files.append(item.name)
        elif item.type == "dir":
            folders.append(item.name)

    return {
        "files": files,
        "folders": folders
    }