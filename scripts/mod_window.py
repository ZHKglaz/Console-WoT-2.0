import Keys
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from gui.Scaleform.framework import ViewSettings, WindowLayer, ScopeTemplates, g_entitiesFactories
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared.utils.key_mapping import getBigworldNameFromKey
from gui import InputHandler
from console.window import ConsoleWindow

def init():
    settings = ViewSettings(ConsoleWindow.alias(), ConsoleWindow, ConsoleWindow.swf(), WindowLayer.WINDOW, None, ScopeTemplates.VIEW_SCOPE)
    g_entitiesFactories.addSettings(settings)
    InputHandler.g_instance.onKeyDown += onhandleKeyEvent

def fini():
    InputHandler.g_instance.onKeyDown -= onhandleKeyEvent
    
def onKeyEvent(event):
      if event.isKeyDown():
           if event.key == Keys.KEY_F10:
               showWindow()
               
def showWindow():
    appLoader = dependency.instance(IAppLoader)
    app = appLoader.getDefLobbyApp()
    app.loadView(SFViewLoadParams(ConsoleWindow.alias()))
