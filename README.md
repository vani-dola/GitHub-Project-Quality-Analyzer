# GitHub Project Quality Analyzer

GitHub Project Quality Analyzer is a Python-based tool that analyzes GitHub repositories and generates a quality report.

## Features

- GitHub repository analysis
- Project structure analysis
- README quality analysis
- Python code quality analysis
- Basic security analysis
- Overall quality score
- Automatic quality report generation

## Requirements

- Python 3.x
- GitHub account
- GitHub Personal Access Token

## Installation

Clone the repository and open the project folder.

Install the required Python packages:

python -m pip install -r requirements.txt

## Usage

Run the following command:

python main.py

Enter a GitHub repository URL when prompted.

Example:

https://github.com/username/repository-name

The analyzer will display:

- Repository details
- Project structure
- README analysis
- Code quality
- Security analysis
- Overall quality score

A complete report is also generated in:

reports/quality_report.txt

## Project Structure

GitHub-Project-Quality-Analyzer/
│
├── analyzer.py
├── github_api.py
├── main.py
├── report_generator.py
├── utils.py
├── requirements.txt
├── README.md
└── reports/

## Security

The project performs basic security checks to identify potentially sensitive files and possible secret-related keywords.

Do not store real passwords, API keys, access tokens, or other sensitive credentials in a public repository.

## Future Improvements

- Web-based user interface
- Interactive quality dashboard
- Advanced code quality metrics
- Improved security detection
- PDF report generation
- GitHub repository comparison
- Deployment as an online application

## License

This project is created for educational and academic purposes.