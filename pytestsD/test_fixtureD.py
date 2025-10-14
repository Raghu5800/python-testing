import pytest

# optimized way to write fixtures for multiples tc's not writing for all fns we can create a class & set fixture for all fns in the class
# u can run the yield side code after all the test cases done we have include scope="class" in conftest file so it will after the all the test are done then one yeild part will be exceuted last like clear cache when closing the browser when testing in done
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture1(self):
        print(" i will run fixture steps in fixture1")

    def test_fixture2(self):
        print(" i will run fixture steps in fixture2")

    def test_fixture3(self):
        print(" i will run fixture steps in fixture3")

    def test_fixture4(self):
        print(" i will run fixture steps in fixture4")