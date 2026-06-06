import re


def check(text: str):

    number_pattern = r"\d+%|\d{4}"

    if re.search(number_pattern, text):

        attribution_words = [
            "study",
            "research",
            "survey",
            "report",
            "according to",
            "source"
        ]

        lower_text = text.lower()

        if not any(word in lower_text for word in attribution_words):
            return (
                True,
                "Specific numerical claim without attribution."
            )

    return False, None