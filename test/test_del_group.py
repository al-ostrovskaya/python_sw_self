def test_del_group(app):
    app.session.login("admin", "secret")
    app.group.delete()
    app.session.logout()
