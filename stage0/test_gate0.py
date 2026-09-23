from gate0 import failed_ids

def test_all_non_none_errors():
    runs = [{"id": 1, "error": 0}, {"id": 2, "error": ""}, {"id": 3, "error": False}]
    assert failed_ids(runs) == [1, 2, 3]


def test_mixed_error_values():
    runs = [{"id": 1, "error": None}, {"id": 4, "error": ""}, {"id": 3}, {"id": 2, "error": 3}, {"id": 5, "error": 3}, {"id": 6}]
    assert failed_ids(runs) == [4, 2, 5]


def test_all_none_or_missing_errors():
    runs = [{"id": 1, "error": None}, {"id": 2, "error": None}, {"id": 3}]
    assert failed_ids(runs) == []


def test_empty_runs():
    runs = []
    assert failed_ids(runs) == []


def test_preserves_input():
    runs = [{"id": 2, "error": ""}, {"id": 1, "error": False}, {"id": 3, "error": 0}, {"id": 5, "error": ""}, {"id": 4, "error": 10}]
    runs_before = [dict(o) for o in runs]

    failed_ids(runs)

    assert runs == runs_before
