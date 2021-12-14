import urllib2

proxy_handler = urllib2.ProxyHandler({'http': 'http://localhost:8080/'})

hp_opener = urllib2.build_opener(proxy_handler)
hp_opener.addheaders = [('x-priority', 'interactive')]

lp_opener = urllib2.build_opener(proxy_handler)

def request_asap(url):
    return hp_opener.open(url)

def request(url):
    return lp_opener.open(url)

if __name__ == "__main__":
    import sys
    priority = 0
    if len(sys.argv) == 3:
        # There's a priority specified:
        priority = int(sys.argv[2])

    url = sys.argv[1]

    if priority:
        request_asap(url)
    else:
        request(url)
