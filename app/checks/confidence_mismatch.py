def check(text: str):

    confidence_words = [
        "definitely",
        "certainly",
        "guaranteed",
        "always",
        "never",
        "undoubtedly"
    ]

    lower_text = text.lower()

    if any(word in lower_text for word in confidence_words):

        evidence_words = [
            "study",
            "research",
            "report",
            "source"
        ]

        if not any(word in lower_text for word in evidence_words):
            return (
                True,
                "Strong confidence language without evidence."
            )

    return False, None