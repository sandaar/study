def permute(s, i):
    n = len(s)
    if i == n - 1 :
        print(i, s)
        return
    for j in range(i, n):
        # print(i, j)
        s[i], s[j] = s[j], s[i]
        permute(s, i + 1)
        s[i], s[j] = s[j], s[i]
          
def permute2(s, i):
    n = len(s)
    if i == 0 :
        print(i, s)
        return
    for j in range(i, -1, -1):
        #print(i, j)
        s[i], s[j] = s[j], s[i]
        permute2(s, i - 1)
        s[i], s[j] = s[j], s[i]

def order(a):
    n = len(a)
    if n in [0, 1]:
        return a
    low = 0
    high = n - 1
    while low <= high:
        if a[low] % 2 == 0:
            a[high], a[low] = a[low], a[high]
            high -= 1
        else:
            low += 1

    for i in range(1, n // 2, 2):
        a[i], a[n - 1 - i] = a[n - 1 - i], a [i]


def permute_alt(s, i):
    n = len(s)
    if i == n - 2:
        print(s)
        return
    for j in range(i, n, 2):
        #print('Before array', s)
        #print('i, j ', i, j)
        s[i], s[j] = s[j], s[i]
        permute_alt(s, i + 1)
        s[i], s[j] = s[j], s[i]
        #print('After array', s)
        #print('i, j ', i, j)

def ok_pos(val, i):
    if (val % 2 == 1 and i % 2 == 0) or (val % 2 == 0 and i % 2 == 1):
        return True
    else:
        return False

def permute_alt2(s, i):
    n = len(s)
    if i == n - 1 :
        print(i, s)
        return
    for j in range(i, n):
        if ok_pos(s[j], i):
            s[i], s[j] = s[j], s[i]
            permute_alt2(s, i + 1)
            s[i], s[j] = s[j], s[i]

def permute_words(s, i):
    n = len(s)
    if i == n - 1:
        if ValidWord(s):
            print(i, s)
            return True
        else:
            return False
    for j in range(i, n):
            s[i], s[j] = s[j], s[i]
            if ValidWordPrefix(s, i + 1):

                permute_words(s, i + 1)
            s[i], s[j] = s[j], s[i]
            return False




if __name__ == '__main__':
    s = ['a', 'b', 'c']
    #permute(s, 0)
    #print('Permute 2')
    #permute2(s, 2)
    a = [1, 3, 2, 4, 7, 6]
    #order(a)
    #print(a)
    #permute_alt(a, 0)
    permute_alt2(a, 0)
