# -*- coding: utf8 -*-
'''
Created on Jan 11, 2010

@author: hidura
'''
# Import Area
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tools.loadKar import core


def application(environ, start_response):
    status = '200 OK'

    response = core(environ)  # Here the assistant takes the parameters and begins the work

    responseData = response.result()  # Here obtaining the result of the assistant
    #responseData={"status":200, "value":Items().Get({"item_name":""}), "type":"text/plain"}
    response_header = None  # Creating the response Header that will contain the type of pay to send.

    if "status" not in responseData and "value" in responseData:
        responseData["status"] = 500
        results = responseData["value"]
        responseData["value"] = [results, "No trajo el status"]
        responseData["type"] = "application/json"
    if "status" not in responseData:
        responseData["status"] = 200

    if int(responseData["status"]) == 301:
        if "type" in responseData:
            Ctype = responseData['type']
        else:
            Ctype = "text/html"

        status = "301 Redirect"
        if "location" not in responseData:
            responseData["location"] = "/"
        response_headers = [('Content-type', "text/html; charset=ISO-8859-1"),
                            ('Location', responseData["location"]), ]

        results = responseData["value"]

    elif int(responseData["status"]) == 200:
        if "type" not in responseData:
            Ctype = "text/html"
        else:
            Ctype = responseData["type"]
        status = "200 OK"

        if Ctype == "application/json":
            results = json.dumps(responseData["value"])
        else:
            results = responseData["value"]
        response_headers = [('Content-type', Ctype + "; charset=ISO-8859-1"),
                            ('Content-Length', str(len(results)))]  # Creating the Header of the data

    elif int(responseData["status"]) == 500:
        if "type" not in responseData:
            Ctype = "text/html"
        else:
            Ctype = responseData["type"]

        results = responseData["value"]

        status = "500 %s" % (results)

        response_headers = [('Content-type', Ctype + "; charset=ISO-8859-1"),
                            ('Content-Length', str(len(results)))]  # Creating the Header of the data


    elif int(responseData["status"]) == 400:
        Ctype = 'text/html'
        results = responseData["value"]

        status = "400"
        response_headers = [('Content-type', Ctype + "; charset=ISO-8859-1"),
                            ('Content-Length', str(len(results)))]  # Creating the Header of the data

    start_response(status, response_headers)  # Sending the Header of the data
    if type(results).__name__ == 'str':
        return [results.encode(encoding='ISO-8859-1')]

    return [results]  # Returning the data to the web page.