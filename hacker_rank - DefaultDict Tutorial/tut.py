from collections import defaultdict

if __name__ == "__main__":

    n, m = list(map(int, input().split()))
    d = defaultdict(list)
    n_vals = [d[input()].append(str(i + 1)) for i in range(n)]
    m_vals = [input() for i in range(m)]

    for v in m_vals:
        if d[v]:
            print(' '.join(d[v]))
            continue
        print(-1)
