def app(environ, start_response):
    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO')

    if method == 'GET' and path == '/ping':
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'pong']
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']