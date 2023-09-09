# class Solution:
#     def furthestDistanceFromOrigin(self, moves: str) -> int:
#         countL, countR, count_ = 0, 0, 0
#         for char in moves:
#             if char == "R":
#                 countR += 1
#             elif char == "L":
#                 countL += 1
#             else:
#                 count_ += 1

#         return (max(countR, countL) + count_ - min(countR, countL))


# class Solution:
#     def minimumPossibleSum(self, n: int, target: int) -> int:
#         resArray = []
#         notIncludable = dict()
#         start = 1
#         while n:
#             if notIncludable.get(start) is None:
#                 notIncludable[target - start] = True
#                 resArray.append(start)
#                 n -= 1
#             start += 1
        
#         return sum(resArray)