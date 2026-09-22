from github_api import connect_github, get_repository
from analyzer import analyze_structure, analyze_code_quality, analyze_readme, analyze_security, calculate_overall_score
from report_generator import generate_report

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

    readme = analyze_readme(repository)

    print("\nREADME Analysis")
    print("----------------------------")
    print("Score:", readme["score"])
    print("Suggestions:", readme["suggestions"])

    quality = analyze_code_quality(repository)

    print("\nCode Quality")
    print("----------------------------")
    print("Score:", quality["score"])
    print("Python Files:", quality["python_files"])
    print("Suggestions:", quality["suggestions"])

    security = analyze_security(repository)

    print("\nSecurity Analysis")
    print("----------------------------")
    print("Score:", security["score"])
    print("Findings:", security["findings"])

    overall_score = calculate_overall_score(readme, quality, security)

    print("\nOverall Quality Score")
    print("----------------------------")
    print("Score:", overall_score, "/100")
    report = generate_report(repository, structure, quality, readme, security, overall_score)

    print("\n")
    print(report)

except Exception as e:
    print("\nError:", e)