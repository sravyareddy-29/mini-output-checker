from app.checks import fabricated_specificity
from app.checks import confidence_mismatch
from app.checks import citation_illusion


def analyze_text(text: str):

    score = 100

    checks = []

    penalties = {
        "fabricated_specificity": 30,
        "confidence_mismatch": 20,
        "citation_illusion": 25
    }

    severities = {
        "fabricated_specificity": "high",
        "confidence_mismatch": "medium",
        "citation_illusion": "medium"
    }

    all_checks = [
        (
            "fabricated_specificity",
            fabricated_specificity.check
        ),
        (
            "confidence_mismatch",
            confidence_mismatch.check
        ),
        (
            "citation_illusion",
            citation_illusion.check
        )
    ]

    for name, func in all_checks:

        fired, reason = func(text)

        checks.append({
            "name": name,
            "severity": severities[name],
            "fired": fired,
            "reason": reason
        })

        if fired:
            score -= penalties[name]

    score = max(score, 0)

    if score >= 80:
        verdict = "clean"
    elif score >= 50:
        verdict = "review"
    else:
        verdict = "suspicious"

    return {
        "trust_score": score,
        "verdict": verdict,
        "checks": checks
    }