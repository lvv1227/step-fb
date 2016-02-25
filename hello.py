def parse(query):
    list=query.split('&')
    for s in list:
        print(s)

def app(environ, start_response):
    """Simplest possible application object"""
    data = ''
    query=environ["QUERY_STRING"]
    list=query.split('&')

    for s in list:
        data+=s+"\n"
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    #print(environ)
    start_response(status, response_headers)
    return iter([data])


