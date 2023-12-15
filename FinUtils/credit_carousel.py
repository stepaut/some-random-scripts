def f(x, tl, ppy):
    if x <= tl:
        return ppy * x / 6
    
    if x <= 2 * tl:
        return (tl + x) * ppy / 12
    
    return 2 * tl * ppy / 6



if __name__ == "__main__":
    limits = []

    print("Write PPY:")
    ppy = float(input()) / 100

    print("Write Transactions limit:")
    tl = float(input())

    print("Write commission per month:")
    com = float(input())

    print("Write your limits separated by spaces:")
    s = input()

    sarr = s.split()
    for ss in sarr:
        limits.append(float(ss))

    reses = [f(l, tl, ppy) for l in limits]

    res = sum(reses) - 2 * com

    print(f'Your income per month: {res / 2}')
