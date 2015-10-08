# -*- coding: utf-8 -*-

from sys import stdout
from time import sleep

def zoid_progress(progress, barLength=40, ascii=False, pad=False):
    """Displays or updates a console progress bar

    Accepts a float between 0 and 1. Any int will be converted to a float.
    A value under 0 represents a 'halt'.
    A value at 1 or bigger represents 100%

    Inputs
    ------
    progress  - Number between 0 and 1
    barLength - Length of the progress bar [40]
    ascii     - Use '#' as the progress indicator, otherwise use a Unicode
                character [False]
    pad       - Pad Zoidberg's claws to stop his head bobbing [False]
    """

    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"

    if barLength < 40:
        barLength = 40
        
    if ascii:
        face = " (;,,,;) "
        ink = "#"
    else:
        face = u" (°,,,°) "
        ink = u"█"

    open_claw   = "(\/)"
    closed_claw = "(|)"

    if int(progress*barLength) % 2:
        pad_ = pad * 0
        left_claw  = open_claw
        right_claw = closed_claw
    else:
        pad_ = pad * 1
        left_claw  = ink*pad + closed_claw
        right_claw = open_claw

    zb = left_claw+face+right_claw
    zb_middle = int(len(zb)/2)
    start = int(round((barLength-zb_middle)*progress))
    
    text = u"\rProgress: [{start}{zb}{rest}] {perc:6.2f}% {stat}".format(
        start=ink*start, zb=zb, perc=progress*100, rest='-'*(barLength-start-zb_middle), stat=status)
    stdout.write(text)
    stdout.flush()
    
if __name__ == "__main__":
    for ii in range(100):
        zoid_progress(ii/99.0)
        sleep(0.1)
    print('')
