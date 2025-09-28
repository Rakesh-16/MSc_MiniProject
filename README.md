# Cloud Financial Data Validator

**Technologies:** Python, Google Cloud Platform (GCP), Gmail API  

An automated system to extract and validate financial data from Gmail using cloud APIs, designed to reduce manual effort, improve accuracy, and streamline financial data processing.

---

## 🚀 Project Overview

The Cloud Financial Data Validator is a Python-based automation project that connects to Gmail via the Gmail API and uses Google Cloud services to process and verify incoming financial data.  

**Key objectives:**
- Automate extraction of financial data from Gmail messages
- Validate data against predefined rules
- Reduce manual processing time and human error

---

## 🗂️ Workflow

The workflow of the system is as follows:

```text
User Gmail Account (Source)
        |
        v
Gmail API (Python) -- Retrieves emails
        |
        v
Email Parsing Module (Python) -- Extracts financial data
        |
        v
Data Validation Module (Python) -- Validates data based on rules
        |
        v
Logging & Reporting Module (Python) -- Stores validation results and generates reports
        |
        v
Google Cloud Platform -- Scalable processing and optional storage
        |
        v
Output / Dashboard -- Final validated data accessible to users
