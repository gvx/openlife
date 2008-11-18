#A OpenLife Text RenderEngine
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
                print "COMMANDS:"
                print 'help         list all commands'
                print 'update       see all changes in the world'
                print 'exit         exit OpenLife'
                print 'save [File]  save game to File (default: auto.sav)'
                print 'load [File]  load a game from File (default: auto.sav)'
            elif s == 'update':
                self.chan.send('SEND UPDATE CHANGES')
                print self.chan.receive()
            elif s == 'exit':
                self.chan.send('KILL *')
            elif s.split()[0] == 'save':
                f = None
                try:
                    f = s.split()[1]
                except:
                    pass
                if not f: f = 'auto.sav'
                self.chan.send('SAVE ' + f)
            elif s.split()[0] == 'load':
                f = None
                try:
                    f = s.split()[1]
                except:
                    pass
                if not f: f = 'auto.sav'
                self.chan.send('LOAD ' + f)
