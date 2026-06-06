# Mini Output Checker

A lightweight FastAPI service that analyzes AI-generated text and returns a structured trust assessment based on potential warning signals commonly found in unreliable AI outputs.

## Project Overview

Large Language Models (LLMs) can generate responses that sound confident and convincing even when information is unsupported or unverifiable.

This project provides a simple trust-analysis layer that evaluates text using a set of heuristic checks and produces:

* A trust score
* An overall verdict
* A detailed breakdown of triggered checks

The goal is not to determine factual truth, but to identify signals that suggest the output may require human review.

---

## API Endpoints

### GET /

Returns a simple welcome message.

### GET /health

Returns the health status of the application.

Example Response:

```json
{
    "status": "healthy"
}
```

### POST /check

Analyzes AI-generated text.

Request:

```json
{
    "text": "87% of users improved productivity."
}
```

Response:

```json
{
    "trust_score": 70,
    "verdict": "review",
    "checks": [
        {
            "name": "fabricated_specificity",
            "severity": "high",
            "fired": true,
            "reason": "Specific numerical claim without attribution."
        }
    ]
}
```

---

## Trust Checks Implemented

### 1. Fabricated Specificity

Detects highly specific numerical claims such as percentages or years that appear without attribution.

Example:

```text
87% of users improved productivity.
```

Why it matters:

AI systems often generate authoritative-looking statistics without citing a source.

---

### 2. Confidence-Evidence Mismatch

Detects strong certainty language when no supporting evidence is provided.

Example:

```text
This definitely solves the problem.
```

Why it matters:

Overconfident statements can make unreliable information appear trustworthy.

---

### 3. Citation Illusion

Detects references to sources or research that cannot be verified.

Example:

```text
According to recent research...
```

Why it matters:

AI-generated content sometimes references studies or sources that are vague, incomplete, or unverifiable.

---

## Trust Score Calculation

The service starts with a trust score of 100.

Each triggered check reduces the score based on severity.

Verdicts are assigned as follows:

| Score Range | Verdict    |
| ----------- | ---------- |
| 80 - 100    | clean      |
| 50 - 79     | review     |
| Below 50    | suspicious |

---

## Project Structure

```text
output-checker/
│
├── app/
│   ├── main.py
│   ├── checker.py
│   ├── schemas.py
│   └── checks/
│       ├── fabricated_specificity.py
│       ├── confidence_mismatch.py
│       └── citation_illusion.py
│
├── tests/
│   └── test_checker.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Running Locally

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Running Tests

```bash
python -m pytest
```

Current result:

```text
3 passed
```

---

## Design Decisions

Instead of attempting full fact-checking, this project focuses on identifying trust signals.

True fact verification requires external knowledge bases, source validation, and web-scale retrieval systems. For a lightweight service, heuristic trust analysis provides a practical first layer of review.

The implemented checks target three common AI failure modes:

* Unsupported numerical claims
* Confidence without evidence
* Unverifiable references

---

## AI Usage Reflection

AI tools were used during development to accelerate implementation and explore possible trust-checking strategies.

One weak suggestion generated during development was a very simple keyword-based approach that treated the presence of certain words as sufficient evidence of suspicious content. After testing, this produced weak results and several false positives.

To improve the solution, the logic was refined to focus on three specific trust signals:

* Fabricated specificity
* Confidence-evidence mismatch
* Citation illusion

This resulted in a more meaningful and interpretable trust assessment system.
