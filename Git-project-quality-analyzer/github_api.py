from github import Github


def connect_github():
    """
    Connect to GitHub without authentication.
    """
    return Github()