# Automated Code Reviewer with Email Feedback (Groq + LangChain)

An automated AI-powered code review system that analyzes Git commits using an LLM and sends structured HTML feedback via email.

This project integrates Groq LLM, LangChain structured output, and GitHub Actions to automatically review code changes and deliver feedback directly to your inbox.

---

# Key Features

* Automatic code review on every push
* Uses Groq LLM (`llama-3.3-70b-versatile`)
* Structured HTML feedback
* Email delivery of review report
* Custom review rules support
* GitHub Actions integration
* Secure environment variables
* Fully automated CI workflow

---

# How This Project is Different

Most AI code reviewers:

* Have fixed review logic
* Do not allow custom rules
* Do not send email feedback automatically
* Require manual execution

This project solves those problems.

## Difference 1: Custom Rule System

You can define your own review rules in:

```python
rule.py
```

Example:

```python
class RuleBook:
    rule = """
Rule 1: The conversation name should be proper, short (4 to 10 words), and easy to understand.
Rule 2: The code should not contain any errors.

Suggestion:
Use colors and proper indentation.
"""
```

You can modify rules anytime without changing the main code.

---

## Difference 2: Automatic Email Feedback

The system automatically sends HTML review reports from:

```
PersonA@gmail.com → PersonB@gmail.com
```

No dashboard needed. No manual checking required.

You receive feedback instantly after pushing code.

---

## Difference 3: Structured HTML Output

The AI generates clean HTML reports:

* Proper formatting
* Easy to read
* Professional layout
* Ready for email delivery

---

## Difference 4: Fully Automated with GitHub Actions

Runs automatically on:

```
git push origin main
```

No manual execution required.

---

# Project Structure

```
project/
│
├── codereviewer.py        # Main script
├── rule.py                # Custom review rules
├── requirements.txt       # Dependencies
├── .env                   # Local environment variables
│
└── .github/
    └── workflows/
        └── python-app.yml # GitHub Actions workflow
```

---

# Installation

## 1. Clone Repository

```
git clone https://github.com/yourusername/ai-code-reviewer.git
cd ai-code-reviewer
```

---

## 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## 3. Create `.env` file

```
GROQ_API_KEY=your_groq_api_key
MAIL_APP_PASSWORD=your_gmail_app_password
```

---

# Required Secrets (GitHub Actions)

Add these secrets in:

GitHub → Repository → Settings → Secrets → Actions

Add:

```
GROQ_API_KEY
MAIL_APP_PASSWORD
```

Changes This:

```
MAIL_FROM 
MAIL_TO
```

---

# Gmail App Password Setup

You must use a Gmail App Password, not your Gmail password.

Steps:

1. Enable 2-Factor Authentication
2. Go to Google Account Settings
3. Security → App Passwords
4. Generate password
5. Use it as MAIL_APP_PASSWORD

---