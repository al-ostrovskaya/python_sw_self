from model.contact import Contact
def test_modify_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify(Contact("first", "middle", "last", "nickname", "title", "company", "address", "home", "mobile",
                            "work", "fax", "email1", "email2", "email3", "1990", "2000", "new_value"))
    app.session.logout()