# -*- coding: utf-8 -*-

import logging
import requests

from .const import (
    HTTP_OK,
    NEXT_ASSET,
    PREVIOUS_ASSET,
    LIST_ASSETS,
    SWITCH_ASSET,
    CURRENT_ASSET,
    ASSET,
    METHOD_GET,
    METHOD_POST,
    METHOD_PUT,
)

_LOGGER = logging.getLogger(__name__)


class Screenly:
    """
    Screenly API class.
    
    Controls the digital signage platform using Python.
    """

    def __init__(self, host, port=80):
        """
        :param str host:        Hostname or IP address of device.
        :param int port:        Port to connect to. Default 80.
        """
        self._host = host
        self._port = port

        #http_proto = 'https' if self._encryption else 'http'

        self._http_url = 'http://{host}:{port}/api'.format(
            host=self._host,
            port=self._port,)

    # helper function that will actually send the request
    def _send_request(self, endpoint, params=None, method=METHOD_GET, version="v1"):

        url = '{url}/{api_version}/{endpoint}'.format(
            url=self._http_url,
            api_version=version,
            endpoint=endpoint)

        if method == METHOD_GET:
            r = requests.get(url, json=params)
        elif method == METHOD_PUT:
            r = requests.put(url, json=params)
        elif method == METHOD_POST:
            r = request.post(url, json=params)
        else:
            return False
        
        if r.status_code == HTTP_OK:
            return r.json()
        else:
            return False

    def next_asset(self):
        """ switches to the next asset in the playlist """
        return self._send_request(NEXT_ASSET)

    
    def previous_asset(self):
        """ switches to the previous asset in the playlist """
        return self._send_request(PREVIOUS_ASSET)

    
    def switch_asset(self, asset_id):
        """ switches to the asset with given its asset id """

        # make sure it's enabled first
        self.enable_asset(asset_id)
        
        return self._send_request(SWITCH_ASSET.format(asset_id=asset_id))


    def current_asset(self):
        """ returns the current active asset """
        return self._send_request(CURRENT_ASSET)


    def list_assets(self):
        """ returns a json object with all the assets """
        return self._send_request(LIST_ASSETS)


    def get_asset_byid(self, asset_id):
        """ returns a json object with the asset information, given the asset id """
        return self._send_request(ASSET.format(asset_id=asset_id))


    def get_asset_byname(self, asset_name):
        """ returns the asset information given the asset name """
        
        for _a in self.list_assets():
            if _a["name"] == asset_name:
                return _a

        return False


    def disable_asset(self, asset_id):
        """ disables asset defined by asset_id """
        _asset_data = self.get_asset_byid(asset_id)
        _asset_data["is_enabled"] = 0

        r = self._send_request(
            ASSET.format(asset_id=asset_id),
            _asset_data,
            METHOD_PUT,
        )

        if not r:
            return False
        else:
            return True


    def enable_asset(self, asset_id):
        """ enables asset defined by asset_id """
        _asset_data = self.get_asset_byid(asset_id)
        _asset_data["is_enabled"] = 1

        r = self._send_request(
            ASSET.format(asset_id=asset_id),
            _asset_data,
            METHOD_PUT,
        )

        if not r:
            return False
        else:
            return True
