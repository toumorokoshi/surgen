from surgen.results import ResultStatus


def test_result_formatting():
    assert str(ResultStatus["PASS"]) == "PASS"
    assert str(ResultStatus["FAIL"]) == "FAIL"
    assert str(ResultStatus["SKIP"]) == "SKIP"
