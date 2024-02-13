import pytest
from application import Application
from group import Group
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
def test_add_group(app):
    app.login("admin", "secret")
    app.create_group(Group("group", "logo", "comment"))
    app.logout()

def test_add_emptygroup(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()
