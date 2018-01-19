# Copyright (c) 2018, Kevin Rodgers
# Released subject to GNU Lesser General Public License v3
# Please see http://www.gnu.org/licenses
import requests
import json
import os

_web_address = os.getenv('NGROK_WEB_ADDR', 'http://127.0.0.1:4040')


class RestClientError(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status
        super(RestClientError, self).__init__(message)


def _build_url(url_route=''):
    return '%s/%s' % (_web_address, url_route)


def post_url(url_route, params):
    headers = {'content-type': 'application/json;charset=UTF-8',
               'Accept': 'application/json'}
    try:
        url = _build_url(url_route=url_route)
        params_str = json.dumps(params).replace(' ', '')
        req = requests.post(url, data=params_str, headers=headers)
        status_code = req.status_code
        if req.headers['content-type'].find("json") < 0:
            response = req.text
        else:
            response = req.json()
    except Exception as e:
        raise RestClientError(str(e), 401)
    return status_code, response


def put_url(url_route, params=None):
    headers = {'content-type': 'application/json'}
    try:
        url = _build_url(url_route=url_route)
        params_str = None if params is None else json.dumps(params)
        req = requests.put(url, data=params_str, headers=headers)
        status_code = req.status_code
        if req.headers['content-type'].find("json") < 0:
            response = req.text
        else:
            response = req.json()
    except Exception as e:
        raise RestClientError(str(e), 400)
    return status_code, response


def get_url(url_route):
    try:
        url = _build_url(url_route=url_route)
        data = requests.get(url)
        status_code = data.status_code
        if data.headers['content-type'].find("json") < 0:
            response = data.text
        else:
            response = data.json()
    except Exception as e:
        raise RestClientError(str(e), 404)
    return status_code, response


def delete_url(url_route):
    try:
        url = _build_url(url_route=url_route)
        data = requests.delete(url)
        status_code = data.status_code
        if data.status_code != 204:
            if data.headers['content-type'].find("json") < 0:
                response = data.text
            else:
                response = data.json()
        else:
            response = {'data': ''}
    except Exception as e:
        raise RestClientError(str(e), 401)
    return status_code, response
