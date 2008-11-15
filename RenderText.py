#OpenLife Text RenderEngine
#You can make your own version if you want for:
# * 3D engines
# * 2D graphics
# * Other text based interfaces
# * Etc.

class Render:
    callonce = True
    def __init__(self, chan):
        self.chan = chan
        self.chan.send('SEND INFO')
        infodict = self.chan.receive()
        print "OpenLife " + '.'.join(str(i) for i in infodict['ver'])
    def __call__(self):
        print "Render call"
        while True:
             s = raw_input("# ")
             if s == 'help':
                 print "You're not getting any."
             elif s == 'update':
                 self.chan.send('SEND UPDATE')
                 print self.chan.receive()
             elif s == 'exit':
                 self.chan.send('KILL *')
