from github_api import connect_github, get_repository
from analyzer import analyze_structure


print("===================================")
print(" GitHub Project Quality Analyzer ")
print("===================================")

github = connect_github()

print("GitHub Connected Successfully!")

repo_url = input("\nEnter GitHub Repository URL: ")

try:
    repository = get_repository(github, repo_url)

    print("\nRepository Details")
    print("----------------------------")
    print("Name:", repository.name)
    print("Owner:", repository.owner.login)
    print("Stars:", repository.stargazers_count)
    print("Forks:", repository.forks_count)
    print("Language:", repository.language)

    structure = analyze_structure(repository)

    print("\nProject Structure")
    print("----------------------------")
    print("Files:", structure["files"])
    print("Folders:", structure["folders"])

except Exception as e:
    print("\nError:", e)