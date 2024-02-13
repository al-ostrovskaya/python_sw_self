import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("first", "middle", "last", "nickname", "title", "company", "address", "home", "mobile",
                            "work", "fax", "email1", "email2", "email3", "1990", "2000"))
    app.session.logout()

