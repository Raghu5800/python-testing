import pytest

# fixtures are used as setup to run before test [eg open browser]
# u can create a conftest file to use it as base class to invoke from there with a func name

# when u define scope as class will run only once when class is initiated & at the end
@pytest.fixture(scope="class")
def setup():
    print("i will run at the beginning")
    yield
    print("i will run at the end")

@pytest.fixture()
def loadData():
    print("Data is being created")
    return ["Raghu", "Raman", "www.google.com"]

# data driven & parameterization can be done with return statements in tuples
@pytest.fixture(params=[("Chrome","Raghuuu", "Raman"), ("Firefox","Raghuu", "Raman"),("Edge", "Raghu","Raman")])
def crossBrowser(request):
    return request.param

# to create html reports for pytest > download from pypi html report & to generate "pytest -v --html=report.html --self-contained-html"