from kivy.app import App
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest

import os
import json
import time

app = App.get_running_app()

def is_json(data):
    try:
        json.loads(data)
    except:
        return False
    return True

def get_data(endpoint, onsuccess=False):
    filepath = app.script_path + '/data/' + endpoint + '.json'
    
    try:
        with open(filepath) as fd:
            jsondata = json.load(fd)
    except (IOError, ValueError) as err:
        # give thread a chance to download and fix data
        time.sleep(2)

    return jsondata
