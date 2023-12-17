from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Jake", "Sully") == "Sully; Jake"
    assert make_full_name("J", "S") == "S; J"
    assert make_full_name("", "") == "; "
    
def test_extract_family_name():
    assert extract_family_name("Sully; Jake") == "Sully"
    assert extract_family_name("S; J") == "S"
    assert extract_family_name("; Jake") == ""
    
def test_exteract_given_name():
    assert extract_given_name("Sully; Jake") == "Jake"
    assert extract_given_name("S; J") == "J"
    assert extract_given_name("Sully; ") == ""
    
pytest.main(["-v", "--tb=line", "-rN", __file__])