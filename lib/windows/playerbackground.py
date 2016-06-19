import contextlib
import kodigui
from lib import util


class PlayerBackground(kodigui.BaseWindow):
    xmlFile = 'script-plex-player_background.xml'
    path = util.ADDON.getAddonInfo('path')
    theme = 'Main'
    res = '1080i'
    width = 1920
    height = 1080

    def __init__(self, *args, **kwargs):
        kodigui.BaseWindow.__init__(self, *args, **kwargs)
        self.background = kwargs.get('background', '')

    def onFirstInit(self):
        self.setProperty('background', self.background)

    @contextlib.contextmanager
    def asContext(self):
        self.show()
        yield
        self.doClose()
