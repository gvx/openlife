class Daemon(object):
    """A "process" running in the background, to maintain important things, that are not always visible.

    Meant to be subclassed."""
    def __init__(self, chan):
        self.chan = chan
    def __call__(self):
        """Subclass at least this function"""
        raise NotImplementedError("__call__ should be subclassed.")
    def __str__(self):
        try:
            return self.info
        except AttributeError:
            return 'DAEMON'

