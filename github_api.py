import os
from github import Github


def connect_github():
    """
    Connect to GitHub using a personal access token.
    """
    token = os.getenv("GITHUB_TOKEN")

    if token:
        return Github(token)

    return Github()


def get_repository(github, repo_url):
    """
    Fetch a GitHub repository using its URL.
    """

    repo_path = repo_url.rstrip("/").split("github.com/")[-1]

    return github.get_repo(repo_path)