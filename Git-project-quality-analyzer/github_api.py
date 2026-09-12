from github import Github


def connect_github():
    """
    Connect to GitHub without authentication.
    """
    return Github()


def get_repository(github, repo_url):
    """
    Fetch a GitHub repository using its URL.
    """

    repo_path = repo_url.rstrip("/").split("github.com/")[-1]

    return github.get_repo(repo_path)