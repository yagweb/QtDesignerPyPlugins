from setuptools import find_packages, setup, Extension
import os
import os.path as osp
import sys
import shutil

try:
    import PyQt5 as PyQt
except:
    import PyQt4 as PyQt

def install_plugins():
    plugin_python_path = osp.join(sys.prefix, 'Library/plugins/designer/python')
    if not os.path.exists(os.path.dirname(plugin_python_path)):
        print('folder %s not exists, is this Ananconda?' % os.path.dirname(plugin_python_path))
        return
    if os.path.exists(plugin_python_path):
        yn = input("folder %s has exists, delete it Y/n?" % plugin_python_path)
        if yn not in ['Y', 'y']:
            print("no python plugin is installed")
            return
        shutil.rmtree(plugin_python_path)
    shutil.copytree('plugins', plugin_python_path)
    print('please add enviroment variable below, for linux export in .bashrc')
    print('PYQTDESIGNERPATH=%s' % (plugin_python_path))

if sys.argv[-1] == 'install':
    install_plugins()

PROJECT_NAME = 'QtDesignerPyPlugins'

setup(name=PROJECT_NAME, version='1.0',
      description='install some Qt Designer plugins for qt designer of Anaconda',
      long_description="""%s installs Qt designer plugins (Matplotlib, ...) for qt designer of Anaconda.
""" % (PROJECT_NAME), 
      py_modules = ['matplotlibwidget', 'qtdesigner_pyplugin'],
      #data_files=['python', 'plugins'],
      requires=[PyQt.__name__, "matplotlib (>1.0)",],
      author = "yagweb",
      url = 'https://github.com/yagweb/QtDesignerPyPlugins')
