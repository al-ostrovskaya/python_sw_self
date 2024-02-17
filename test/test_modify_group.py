from model.group import Group
def test_modify_name(app):
    app.session.login("admin", "secret")
    app.group.test_modify_name(Group(name="New_name"))
    app.session.logout()
def test_modify_header(app):
    app.session.login("admin", "secret")
    app.group.test_modify_name(Group(header="New_header"))
    app.session.logout()