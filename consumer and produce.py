def consumer():
    r = ''
    while True:
        n = yield r
        if not n :
            return
        print('[consumer] consumer %s' % n)
        r = '200 ok'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n+1
        print('[produce] produce %s' % n)
        r = c.send(n)
        print('[produce] consumer return %s' % r)
    c.close()

c = consumer()
produce(c)
