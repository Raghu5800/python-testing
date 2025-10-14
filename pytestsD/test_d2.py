import pytest


def test_thirdpgm():
    print("thirdpgm new test file")
    msg = "hello world"
    assert msg == "hello world"


def test_fourthpgm():
    a= 10
    b= 20
    assert a+20 == 40, "Doesn't match"

# to run specific test function just give py.test -k (func name - fourthpgm) -v -s
# -k stands for method wise execution
# to run multiple fn test cases from diff file just use mark concept @pytest.mark.smoke [eg] & in cmd py.test -m smoke -v -s
@pytest.mark.smoke
@pytest.mark.skip
def test_fifthdpgm():
    print("fifth new test file")
    msg = "hello world"
    assert msg == "hello world"

@pytest.mark.smoke
@pytest.mark.xfail
def test_sixthpgm():
    print("sixth new test file")
    msg = "hello world"
    assert msg == "hello world"

