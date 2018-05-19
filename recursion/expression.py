# Complete the function below.
import re

def sanitize(array):
    s = ''.join(array)
    s = re.sub(r'\b0+(?!\b)', '', s)
    s = s.rstrip('*')
    s = s.rstrip('+')
    return s


def generate(array, i, target, result):
    n = len(array)
    if i == n:
        s = sanitize(array)
        print(s)
        if eval(s) == target:
            result.append(s)
        return
    
    s = sanitize(array[:i+1])
    if eval(s) > target:
        return
    if array[i] == '':
        array[i] = '*'
        generate(array, i + 1, target, result)
        array[i] = '+'
        generate(array, i + 1, target, result)
        array[i] = ''
        generate(array, i + 1, target, result)
    else:
        generate(array, i + 1, target, result)

    
    
    
def generate_all_expressions(s, target):
    result = []
    array = []
    for i in range(len(s)):
        array.append(s[i])
        if i != len(s) - 1:
            array.append('')
    print('Initial array ', array)
    generate(array, 0, target, result)
    print('Result array', result)
    return result

if __name__ == '__main__':
    s = '222'
    target = 24
    generate_all_expressions(s, target)
