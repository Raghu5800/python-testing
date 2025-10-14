# pytest file & methods should start with (test_)  ** mandatory or should end with test_
# to write pytest u should use function only
# to run pytest setup run config & path of the file & run it
# to run the pytest with more info & logs go to pytest folder & enter "py.test -v -s"
import pytest


@pytest.mark.smoke
def test_firstpgm():
    print("firstpgm")


def test_secondpgm():
    print("secondpgm")


def test_thirdpgm():
    print("thirdpgm")



def test_fourthpgm():
    print("fourthpgm")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
