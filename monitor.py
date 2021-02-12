import sys
import pyautogui
import time
import pygetwindow as gw
import xml.etree.ElementTree as ET
from pywinauto.keyboard import send_keys
from pywinauto import application
from pywinauto.application import Application
from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError

tree = ET.parse('monitor.xml')
root = tree.getroot()

targets = root.findall("./monitor-run-task/variables/targets/target")

for app in targets:
  appname = app.text

  try:
    app = application.Application()
    app.start(appname)
    # Do stuff to validate the application is working great
    time.sleep(3)
    app.kill()

    DEFAULT_METRIC_PREFIX="name=Custom Metrics|AppLauncher|" + appname + "|Launch Status,value=1"
    print(DEFAULT_METRIC_PREFIX)
  except Exception as e:
    print(e)
