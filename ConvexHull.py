from functools import cmp_to_key

mid = [0, 0]

def quad(p):
    if p[0] >= 0 and p[1] >= 0:
        return 1
    if p[0] <= 0 and p[1] >= 0:
        return 2
    if p[0] <= 0 and p[1] <= 0:
        return 3
    return 4

def orientation(a, b, c):
    res = (b[1]-a[1]) * (c[0]-b[0]) - (c[1]-b[1]) * (b[0]-a[0])
    if res == 0:
        return 0
    return 1 if res > 0 else -1

def compare(p1, q1):
    p = [p1[0]-mid[0], p1[1]-mid[1]]
    q = [q1[0]-mid[0], q1[1]-mid[1]]
    one, two = quad(p), quad(q)
    if one != two:
        return -1 if one < two else 1
    return -1 if p[1]*q[0] < q[1]*p[0] else 1

def merger(a, b):
    n1, n2 = len(a), len(b)
    ia, ib = max(range(n1), key=lambda i: a[i][0]), min(range(n2), key=lambda i: b[i][0])
    inda, indb, done = ia, ib, False

    while not done:
        done = True
        while orientation(b[indb], a[inda], a[(inda+1) % n1]) >= 0:
            inda = (inda + 1) % n1
        while orientation(a[inda], b[indb], b[(n2+indb-1) % n2]) <= 0:
            indb = (indb - 1) % n2
            done = False

    uppera, upperb, inda, indb, done = inda, indb, ia, ib, False

    while not done:
        done = True
        while orientation(a[inda], b[indb], b[(indb+1) % n2]) >= 0:
            indb = (indb + 1) % n2
        while orientation(b[indb], a[inda], a[(n1+inda-1) % n1]) <= 0:
            inda = (inda - 1) % n1
            done = False

    lowera, lowerb, ret, ind = inda, indb, [a[uppera]], uppera

    while ind != lowera:
        ind = (ind+1) % n1
        ret.append(a[ind])

    ind = lowerb
    ret.append(b[lowerb])
    while ind != upperb:
        ind = (ind+1) % n2
        ret.append(b[ind])

    return ret

def bruteHull(a):
    global mid
    s = set()
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            x1, x2, y1, y2 = a[i][0], a[j][0], a[i][1], a[j][1]
            a1, b1, c1 = y1-y2, x2-x1, x1*y2-y1*x2
            pos, neg = 0, 0
            for k in range(len(a)):
                if k in {i, j} or (a1*a[k][0]+b1*a[k][1]+c1 <= 0):
                    neg += 1
                if k in {i, j} or (a1*a[k][0]+b1*a[k][1]+c1 >= 0):
                    pos += 1
            if pos == len(a) or neg == len(a):
                s.update({tuple(a[i]), tuple(a[j])})

    ret, mid = [list(x) for x in s], [sum(x[0] for x in s)/len(s), sum(x[1] for x in s)/len(s)]
    ret.sort(key=cmp_to_key(compare))
    return ret

def divide(a):
    if len(a) <= 5:
        return bruteHull(a)

    mid = len(a) // 2
    left_hull, right_hull = divide(a[:mid]), divide(a[mid:])
    return merger(left_hull, right_hull)

def get_convex_hull(cities):
    cities.sort()
    return [tuple(point) for point in divide(cities)]

