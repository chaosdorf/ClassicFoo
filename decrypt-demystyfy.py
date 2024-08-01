#!/usr/bin/env python3
#
# Provides the TLS-encrypted, JSONified data of chaosdorf.de/~ytvwld/freitagsfoo.json in a simple, readable format.
#

from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import logging
import json

freitagsfooURL = "https://chaosdorf.de/~ytvwld/freitagsfoo.json"

def getTalks():
    r = requests.get(freitagsfooURL)
    if r.status_code != 200:
        logging.error(f"Failed to get talks: code {r.status_code} received\n")
        return
    data = json.loads(r.text)
    if "talks" not in data:
        logging.error("Failed to read talks: no talks found\n")
        return
    out = ""
    for t in data["talks"]:
        speaker = ", ".join(t["persons"])
        out += speaker + ";;;" + t['title'] + "\n"
    return out

def getInfo():
    r = requests.get(freitagsfooURL)
    if r.status_code != 200:
        logging.error(f"Failed to get info: code {r.status_code} received\n")
        return
    data = json.loads(r.text)
    if "hosts" not in data or "date" not in data:
        logging.error("Failed to read info: no info found\n")
        return
    hosts = ", ".join(data["hosts"])
    return f"{hosts};;;{data['date']}"

class TheHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/talks":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(getTalks().encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(getInfo().encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 - not found")

def runServer():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, TheHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    runServer()
