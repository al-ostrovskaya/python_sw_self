from model.group import Group
def test_modify_group(app):
    app.session.login("admin", "secret")
    app.group.modify(Group("", "", "", "modify_name", "modify_header", "modify_footer"))
    app.session.logout()