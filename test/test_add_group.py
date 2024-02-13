import pytest
from fixture.application import Application
from model.group import Group
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("group", "logo", "comment"))
    app.session.logout()

def test_add_emptygroup(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
