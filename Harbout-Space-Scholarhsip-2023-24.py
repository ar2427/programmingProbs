# # https://codeforces.com/contest/1864

# t = int(input())

# for tc in range(t):
#     x, y, n = map(int, input().split())
#     a = []

#     diff = 1
#     a.append(y)
#     for numInd in range(1, n - 1):
#         a.append(a[numInd - 1] - diff)
#         diff += 1
    
#     a.append(x)
#     if a[-2] - a[-1] < diff:
#         print(-1)
#     else:
#         for i in a[::-1]:
#             print(i, end=" ")
#         print("")