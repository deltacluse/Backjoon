# 1193 분수찾기


def main():
    X = int(input())
    temp = 0
    i = 1
    while temp < X:
        temp += i
        i += 1

    # a: 분자, b: 분모, c: +-
    if i % 2 == 1:
        a = i-1
        b = 1
        c = 1
    else:
        a = 1
        b = i-1
        c = -1

    while temp > X:
        a -= c
        b += c
        temp -= 1

    print(str(a) + "/" + str(b))


if __name__ == "__main__":
    main()
