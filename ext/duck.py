import stackless

def run_duck():
    global DUCKCOUNT
    while DUCKCOUNT < 30:
        print "It's a duck!"
        DUCKCOUNT += 1
        stackless.schedule()

def prepare_duck(chan):
    global DUCKCOUNT
    DUCKCOUNT = 0
    global DUCKCHAN
    DUCKCHAN = chan

DICT = {'run': run_duck,
        'init': prepare_duck,
        'info': 'A duck. An OpenLife extension which does nothing.'}