from app.checker import analyze_text


def test_fabricated_specificity():

    result = analyze_text(
        "87% of users improved productivity."
    )

    assert result["trust_score"] < 100


def test_confidence_mismatch():

    result = analyze_text(
        "This definitely solves the problem."
    )

    assert result["trust_score"] < 100


def test_clean_text():

    result = analyze_text(
        "Python is a programming language."
    )

    assert result["verdict"] == "clean"