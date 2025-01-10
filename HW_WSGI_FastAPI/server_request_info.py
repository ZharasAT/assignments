def app(environ, start_response):
    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO')
    protocol = environ.get('SERVER_PROTOCOL')
    url = environ.get('wsgi.url_scheme') + "://" + environ.get('HTTP_HOST') + environ.get('PATH_INFO')

    if method == 'GET' and path == '/info':
        response_body = f"""
        HTTP Method: {method},
        Request URL: {url},
        Protocol: {protocol}
        """

        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [response_body.encode('utf-8')]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']