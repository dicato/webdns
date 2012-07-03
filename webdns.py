from bottle import route, run
import dns.resolver

@route('/')
@route('/:name')
def index(name='www.google.com'):
    return str(dns.resolver.query(name).response)

run(host='localhost', port=8080)
