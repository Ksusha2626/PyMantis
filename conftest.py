from fixture.application import Application
import pytest
import json
import os.path

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def destroy(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.stop()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


# @pytest.fixture(scope="session")
# def orm(request):
#     db_config = load_config(request.config.getoption("--target"))['db']
#     db_fixture_orm = ORMfixture(host=db_config['host'], name=db_config['name'],
#                                 user=db_config['user'], password=db_config['password'])
#     return db_fixture_orm
