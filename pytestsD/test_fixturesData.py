import pytest

@pytest.mark.usefixtures("loadData")
class TestExample2:

    def test_editProfile(self, loadData):
        print(loadData[0])
        print(loadData[1])
        print(loadData[2])

