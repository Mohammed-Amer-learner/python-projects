# Jira Project Info Fetcher

This script connects to the Jira Cloud REST API and retrieves details about your Jira projects.

## 📋 Features

* Authenticates with Jira using an API token
* Fetches a list of projects from your Jira workspace
* Parses and displays project details, such as project name

## 🔧 Requirements

* Python 3.x
* `requests` library

Install dependencies:

```bash
pip install requests
```

## 🚀 Usage

### 1. Clone or download the script.

### 2. Set your Jira credentials

Replace:

```python
API_TOKEN = "Add api key"
```

with your actual Jira API token.

### 3. Run the script

```bash
python fetch_jira_projects.py
```

### 4. Output

The script will output formatted JSON of all your Jira projects, and then print the name of the first project.

### Example Output

```json
[
    {
        "id": "10000",
        "key": "PROJ",
        "name": "Sample Project",
        ...
    }
]
```

Then prints:

```
Sample Project
```

## 🛡️ Security

* **Never commit your API token to version control.**
* Use environment variables or a `.env` file to store sensitive credentials if deploying.

## 📘 References

* [Jira REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)

---

Let me know if you’d like a `.env` version of this setup, or want this wrapped in a command-line tool.
