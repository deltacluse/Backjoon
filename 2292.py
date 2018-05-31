# 2292 벌집


def make_list(N):
    temp = 1
    l_room = []
    i = 1
    while temp < N:
        l_room.append(temp)
        temp += i*6
        i += 1
    return l_room


def main():
    N = int(input())
    l_room = make_list(N)
    print(len(l_room)+1)


if __name__ == "__main__":
    main()
