"""
A Matplotlib Figure widget plugin for Qt Designer
"""

import os.path as osp

from matplotlib import rcParams
rcParams['font.size'] = 9

from qtdesigner_pyplugin import create_qtdesigner_pyplugin
Plugin = create_qtdesigner_pyplugin("Matplotlib", "matplotlibwidget",
              "MatplotlibWidget",
              icon = osp.join(rcParams['datapath'], 'images', 'matplotlib.png'), 
              tooltip = 'matplotlib figure widget')