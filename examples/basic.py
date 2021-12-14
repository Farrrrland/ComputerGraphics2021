from twisted.internet import reactor
from turtle import proxy, config

s = """\
# defaults is pulled out of the end results
# and used to fill hostnames with missing
# parameters
defaults: &defaults
    # calls that can be made inside the interval of time
    calls: 1

    # interval is specified in seconds
    interval: 1

    # the number of concurrent calls that we are allowed to
    # have running at any given time.
    concurrency: 10

delicious.com:
    <<: [*defaults]

www.google.com:
    calls: 5
    interval: 1

filter-rest: True
port: 8080
"""

urlmap, rest, port = config.loadConfigFromString(s)
f = proxy.TurtleHTTPFactory(urlmap, rest)
reactor.listenTCP(port, f)
reactor.run()
