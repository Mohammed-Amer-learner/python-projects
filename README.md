# 🐍 Python Projects by Mohammed Amer

Welcome! This repository contains beginner-friendly Python projects that demonstrate my learning and practical implementation of core Python concepts. These mini-projects are simple, command-line based tools built using pure Python and standard libraries.

---

## 📁 Projects Included

### 1. 📂 File Lister

A Python script that lists all files inside specified folders and handles common errors like missing folders or permission issues.

* **Key Features:**

  * Uses `os` module to read directories
  * Handles `FileNotFoundError` and `PermissionError`
  * Customizable folder paths

📄 [View File Lister README](file_lister/README.md)

---

### 2. 🧮 Command-Line Calculator

A simple calculator that performs basic operations (add, sub, mul, div) using command-line arguments.

* **Key Features:**

  * Uses `sys.argv` for input
  * Supports addition, subtraction, multiplication, and division
  * Handles basic input parsing

📄 [View Calculator Script](calculator/calculator.py)

---

### 3. 🐙 GitHub PR UserID Fetcher

A Python script that fetches the user ID of the creator of the latest pull request from a specified GitHub repository using the GitHub API.

* **Key Features:**

  * Uses `requests` library to make HTTP GET requests
  * Parses JSON responses from GitHub API
  * Extracts user login and ID from PR data

📄 [View GitHub PR UserID Fetcher Script](github_pr_userid_fetcher/pr_user_fetcher.py)

---

### 4. ☁️ Boto3 AWS DevOps Automation Scripts

A collection of automation scripts using `boto3` for managing AWS resources. These scripts help in daily DevOps activities such as EC2 management, S3 bucket operations, IAM tasks, and more.

* **Key Features:**

  * Automates tasks like starting/stopping EC2, snapshot cleanup, S3 encryption
  * Designed for Lambda compatibility
  * IAM-secure and scalable

📄 [View Boto3 Automation Scripts](boto3_aws_devops/README.md)

---

## 📌 Requirements

* Python 3.x
* Standard libraries (`os`, `sys`, etc.)
* `requests` library (`pip install requests`) – for GitHub PR Fetcher
* `boto3` library (`pip install boto3`) – for AWS DevOps automation
* AWS credentials configured for Boto3-based scripts
* Internet access (for GitHub API and AWS calls)

---

## 👤 Author

**Mohammed Amer**
📍 Hyderabad, India
📧 [mohammedamer9553@gmail.com](mailto:mohammedamer9553@gmail.com)
🔗 *LinkedIn to be added soon*

---

## 📝 License

MIT License — feel free to use, modify, and share these projects for learning or personal use.
