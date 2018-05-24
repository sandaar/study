
import logging
import sys

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.level = logging.INFO
logger.addHandler(handler)

def find_max_length_of_matching_parentheses(brackets):
    n = len(brackets)
    if n <= 1:
        return 0
    closed = 0
    size = max_size = 0

    for i in range(n - 1, -1, -1):
        logger.debug("i = {0}\nBrackets[{0}]: {1}".format(i, brackets[i]))
        if brackets[i] == ')':
            closed += 1
        else:
            if closed > 0:
                size += 2
                max_size = max(size, max_size)
                closed -= 1
            else:
                size = 0
                closed = 0

        logger.debug('Closed {}'.format(closed))
        logger.debug('Size {}'.format(size))
        logger.debug('Max size {}\n\n'.format(max_size))
    return max_size
