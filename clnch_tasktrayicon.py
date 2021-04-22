import ckit

class TaskTrayIcon( ckit.TaskTrayIcon ):

    def __init__( self, console_window, parent_window ):

        ckit.TaskTrayIcon.__init__( self,
            title = "CraftLaunch",
            )

        self.console_window = console_window
        self.parent_window = parent_window
