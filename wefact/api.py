#!/usr/bin/env python

import sys
import requests
import simplejson as json
import datetime

class WeFactAPI():
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def sendRequest(self, controller, action, params = {}):
        params['api_key']    = self.api_key
        params['controller'] = controller
        params['action']     = action
        

        r = requests.post(self.url, data=params, verify=False)
        try:
            ret =  r.json()
        except ValueError, e:
            ret = {}
            ret['controller'] = 'invalid'
            ret['action']     = 'invalid'
            ret['status']     = 'error'
            ret['date']       = datetime.datetime.now()
            ret['errors']     = [ r.text ]

        return ret


    def prepareParams(self, params):
        ret = []
        for k in params.keys():
            ret.append(str(k)+"="+str(params[k]))

        return '&'.join(ret);
