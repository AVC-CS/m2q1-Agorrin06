def getPivot(number):
    avg = sum(number) / len(number)

    best_idx = 0
    best_diff = float("inf")

    for i, x in enumerate(number):
        d = abs(x - avg)

        if d <= best_diff:
            best_diff = d
            best_idx = i 
    return number[best_idx], best_idx

def split(number):
    pivot, pidx = getPivot(number)

    left, right = [], []
    for i, x in enumerate(number):
        if i == pidx:
            continue
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return left + [pivot] + right


def main():
    # number = list(map(int, input().split()))
    number = [65, 15, 10, 20, 40, 55]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
