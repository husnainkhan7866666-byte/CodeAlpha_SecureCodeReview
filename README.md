# CodeAlpha_SecureCodeReview
 **Secure Code Review Project
 Overview**

This project demonstrates a secure code review process on a Python-based application. The objective is to identify security vulnerabilities and provide remediation techniques.

**Tools Used**
Python
Bandit (Static Code Analysis)
Identified Vulnerabilities
Hardcoded credentials
Command injection (use of shell=True)
Lack of input validation
**Remediation?**
Removed hardcoded passwords
Avoided unsafe command execution
Implemented input validation
**How to Run**
Run vulnerable code:
python3 app.py
Run secure version:
python3 secure_app.py

**Run Bandit:**
bandit -r .

**Learning Outcomes**
Understanding secure coding practices
Identifying vulnerabilities using tools
Applying remediation techniques

**Disclaimer**
This project is for educational purposes only.
