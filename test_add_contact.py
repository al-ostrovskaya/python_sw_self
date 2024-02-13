from application import Application
from contact import Contact
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact("first", "middle", "last", "nickname", "title", "company", "address", "home", "mobile",
                            "work", "fax", "email1", "email2", "email3", "1990", "2000"))
    app.logout()

