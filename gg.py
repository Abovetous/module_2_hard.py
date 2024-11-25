def password (n):
    string = ""
    for i in range(1,21):
        for j in range(i + 1,21):
            d = i + j
            if n % d == 0:
                string += f"{i}{j}"
    return string
k = int(input())
if 3 <= k <= 20:
    print(password(k))
