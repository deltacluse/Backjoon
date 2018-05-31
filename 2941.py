# 2941 크로아티아 알파벳

def main():
    s_in = input()  # 입력 문자열

    l_cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]  # 크로아티아 알파벳

    # 크로아티아 알파벳을 a로 바꿔 개수 확인
    for i in l_cro:
        s_in = s_in.replace(i, 'a')
    print(len(s_in))


if __name__ == "__main__":
    main()
