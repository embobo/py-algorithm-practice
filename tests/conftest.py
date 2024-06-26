from pathlib import Path

import pytest

DATA_PATH = Path("tests/data")


@pytest.fixture()
def hackerrank_array_manipulation_case_2() -> str:
    path = DATA_PATH / "hackerrank" / "array_manipulation" / "case_2.txt"
    with open(path, "r") as f:
        return f.read()


@pytest.fixture()
def hackerrank_array_manipulation_case_7() -> str:
    path = DATA_PATH / "hackerrank" / "array_manipulation" / "case_7.txt"
    with open(path, "r") as f:
        return f.read()
