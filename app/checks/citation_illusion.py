import re


def check(text: str):

    pattern = r"(according to|source:)"

    if re.search(pattern, text.lower()):

        if "http" not in text and "www." not in text:

            return (
                True,
                "Citation mentioned but not verifiable."
            )

    return False, None