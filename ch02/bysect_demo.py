import bisect, sys

HAYSTACK = [1,4,5,6,7,8,9,12,13,15,20,26,29]
NEEDLES = [0,1,2,5,8,10,12,22,23,29,30,31]

ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == "__main__":
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right

    print('DEMO: ', bisect_fn.__name__)
    print('haystack ->', ' '.join("%2d" % n for n in HAYSTACK))
    demo(bisect_fn)