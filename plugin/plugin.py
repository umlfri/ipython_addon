from org.umlfri.api.main_loops.qt import QtMainLoop


def plugin_main(app):
    import inprocess_qtconsole
    app.set_main_loop(QtMainLoop())
    inprocess_qtconsole.main(i=app)
