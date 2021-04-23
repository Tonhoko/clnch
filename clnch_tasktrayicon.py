import ckit
import pyauto

class TaskTrayIcon( ckit.TaskTrayIcon ):

    def __init__( self, console_window, parent_window ):

        ckit.TaskTrayIcon.__init__( self,
            title = "CraftLaunch",
            rbuttonup_handler = self._onRightButtonUp,
            )

        self.console_window = console_window
        self.parent_window = parent_window

    def _onRightButtonUp( self, x, y, mod ):

        def onExit( info ):
            self.parent_window.quit_requested = True
            self.parent_window.quit()

        menu_items = []

        menu_items.append( ( "Quit", onExit ) )

        x, y = pyauto.Input.getCursorPos()
        self.popupMenu( x, y, menu_items )
