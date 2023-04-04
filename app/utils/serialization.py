# -*- coding: utf-8 -*-

from flask import jsonify
from datetime import datetime

# API response
def jsonify_with_data(err, **kwargs):
    resp = {'data': kwargs, 'message': err[1], 'code': err[0], 'time': datetime.now().timestamp()}
    return jsonify(resp), err[0]


def jsonify_with_error(err, errors=None):
    resp = {'message': err[1], 'code': err[0], 'time' : datetime.now().timestamp()}
    return jsonify(resp), err[0]
