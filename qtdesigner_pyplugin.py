from PyQt5.QtGui import QIcon
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
import os.path as osp
import os

images_path = os.environ.get("PYQTDESIGNERPATH", None)
nf_image_path = os.path.join(images_path, "not_found.png")
if images_path is None or not os.path.isfile(nf_image_path):
    default_icon = QIcon()
else:
    default_icon = QIcon(nf_image_path)

def create_qtdesigner_pyplugin(group, module_name, class_name, widget_options = {},
                             icon = None, tooltip = "", whatsthis = ""):
    """Return a custom QtDesigner plugin class    
    Example:
    create_qtdesigner_pyplugin("Matplotlib", "matplotlibwidget",
              "MatplotlibWidget",
              icon = osp.join(rcParams['datapath'], 'images', 'matplotlib.png'), 
              tooltip = 'matplotlib figure widget')
    """
    Widget = getattr(__import__(module_name, fromlist=[class_name]), class_name)
    
    class CustomWidgetPlugin(QPyDesignerCustomWidgetPlugin):
        def __init__(self, parent = None):
            QPyDesignerCustomWidgetPlugin.__init__(self)
            self.initialized = False
    
        def initialize(self, core):
            if self.initialized:
                return
            self.initialized = True
    
        def isInitialized(self):
            return self.initialized
        
        def createWidget(self, parent):
            return Widget(parent, **widget_options)
        
        def name(self):
            return class_name
        
        def group(self):
            return group
        
        def icon(self):
            if icon is None or not osp.isfile(icon):
                return default_icon
            else:
                return QIcon(icon)
            
        def toolTip(self):
            return tooltip
        
        def whatsThis(self):
            return whatsthis
        
        def isContainer(self):
            return False
        
        def domXml(self):
            return '<widget class="%s" name="%s" />\n' % (class_name,
                                                          class_name.lower())
        def includeFile(self):
            return module_name

    return CustomWidgetPlugin