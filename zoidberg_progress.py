#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdout
from time import sleep
import argparse

def zoidberg_progress(progress, bar_length=40, ascii=False, pad=False, food='-', woop=False):
    """Displays or updates a console progress bar

    Accepts a float between 0 and 1. Any int will be converted to a float.
    A value under 0 represents a 'halt'.
    A value at 1 or bigger represents 100%

    Inputs
    ------
    progress  - Number between 0 and 1
    bar_length - Length of the progress bar [40]
    ascii     - Use '#' as the progress indicator, otherwise use a Unicode
                character [False]
    pad       - Pad Zoidberg's claws to stop his head bobbing [False]
    food      - Symbol for Zoidberg to be chasing, should be length one string ['-']
    woop      - Zoidberg woops instead of inks [False]
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

    if bar_length < 40:
        bar_length = 40

    if ascii:
        face = " (;,,,;) "
        ink = "#"
    else:
        face = u" (°,,,°) "
        ink = u"█"

    open_claw   = "(\/)"
    closed_claw = "(|)"

    if int(progress*bar_length) % 2:
        pad_ = pad * 0
        left_claw  = open_claw
        right_claw = closed_claw
    else:
        pad_ = pad * 1
        left_claw  = ink*pad + closed_claw
        right_claw = open_claw

    zb = left_claw+face+right_claw
    zb_middle = int(len(zb)/2)
    start = int(round((bar_length-zb_middle)*progress))
    rest  = bar_length-start-zb_middle-pad_

    if woop:
        ink=("woop"*int(1+start/4))[:start]
    else:
        ink = ink*start

    text = u"\rProgress: [{start}{zb}{rest}] {perc:6.2f}% {stat}".format(
        start=ink, zb=zb, perc=progress*100, rest=food*rest, stat=status)
    stdout.write(text)
    stdout.flush()

def test():
    for ii in range(100):
        zoidberg_progress(ii/99.0)
        sleep(0.1)
    print('')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Zoidberg progress bar')
    parser.add_argument('progress', metavar='progress', nargs='?', type=float,
                        help="Number between 0 and 1")
    parser.add_argument('-l', '--length', dest='bar_length', help="Length of the progress bar",
                        default=40, action='store')
    parser.add_argument('-a', '--ascii', help="Use '#' as the progress indicator, otherwise use a Unicode character",
                        default=False, action='store_true')
    parser.add_argument('-p', '--pad', help="Pad Zoidberg's claws to stop his head bobbing",
                        default=False, action='store_true')
    parser.add_argument('-f', '--food', help="Symbol for Zoidberg to be chasing, should be length one string",
                        nargs=1, default='-', action='store')
    parser.add_argument('-w', '--woop', help="Zoidberg woops instead of inks",
                        default=False, action='store_true')
    parser.add_argument('-t', '--test', help="Run test", default=False, action='store_true')

    args = parser.parse_args()

    if args.test:
        test()
    else:
        zoidberg_progress(args.progress,
                          bar_length=args.bar_length,
                          ascii=args.ascii,
                          pad=args.pad,
                          food=args.food,
                          woop=args.woop)
