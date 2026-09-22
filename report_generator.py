def generate_report(repository, structure, code_quality, readme, security, overall_score):
    report = []

    report.append("GitHub Project Quality Report")
    report.append("=" * 40)

    report.append("\nRepository Details")
    report.append("-" * 30)
    report.append(f"Name: {repository.name}")
    report.append(f"Owner: {repository.owner.login}")
    report.append(f"Stars: {repository.stargazers_count}")
    report.append(f"Forks: {repository.forks_count}")
    report.append(f"Language: {repository.language}")

    report.append("\nProject Structure")
    report.append("-" * 30)
    report.append(f"Files: {structure['files']}")
    report.append(f"Folders: {structure['folders']}")

    report.append("\nREADME Analysis")
    report.append("-" * 30)
    report.append(f"Score: {readme['score']}/100")
    report.append(f"Suggestions: {readme['suggestions']}")
    report.append("\nCode Quality")
    report.append("-" * 30)
    report.append(f"Score: {code_quality['score']}/100")
    report.append(f"Python Files: {code_quality['python_files']}")
    report.append(f"Total Lines: {code_quality['total_lines']}")
    report.append(f"Suggestions: {code_quality['suggestions']}")

    report.append("\nSecurity Analysis")
    report.append("-" * 30)
    report.append(f"Score: {security['score']}/100")
    report.append(f"Findings: {security['findings']}")

    report.append("\nOverall Quality Score")
    report.append("-" * 30)
    report.append(f"Score: {overall_score}/100")
    report_text = "\n".join(report)

    with open("reports/quality_report.txt", "w", encoding="utf-8") as file:
        file.write(report_text)

    return report_text