from pystringtoolkit.case_conversion import invert_cases
#Testing the inverse case
def test_invert_cases():
    assert invert_cases("Hello") == "hELLO"
    assert invert_cases("hELLO") == "Hello"
    assert invert_cases("CASEinversion") == "caseINVERSION"
    assert invert_cases("Mukesh1352") == "mUKESH1352"
