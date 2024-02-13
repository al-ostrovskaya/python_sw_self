from model.group import Group

def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("group", "logo", "comment", "","",""))
    app.session.logout()

def test_add_emptygroup(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", "", "","",""))
    app.session.logout()


