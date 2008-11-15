#OpenLife Soya RenderEngine
#You can make your own version if you want for:
# * Other 3D engines
# * 2D graphics
# * Text based interface
# * Etc.
import soya

class Render:
    callonce = True
    def __init__(self, chan):
        self.chan = chan
    def __call__(self):
        print 'RenderEngine not ready.'
        self.chan.send('KILL *')
