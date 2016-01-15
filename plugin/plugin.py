from functools import partial

from org.umlfri.api.main_loops.qt import QtMainLoop


class Terminal:
    def __init__(self, app):
        self.__app = app
    
    def open(self):
        import inprocess_qtconsole
        
        self.__app.actions["open"].enabled = False
        self.__app.actions["open"].triggered.disconnect(self.open)
        inprocess_qtconsole.main(i=self.__app)


def get_main_loop():
    return QtMainLoop()


def plugin_main(app):
    app.actions["open"].triggered.connect(Terminal(app).open)
