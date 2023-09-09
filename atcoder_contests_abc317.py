# Link :  https://atcoder.jp/contests/abc317

# Qn 1

# N, H, X = list(map(int, input().split()))

# potions = list(map(int, input().split()))

# for ind in range(len(potions)):
#     if H + potions[ind] >= X:
#         print(ind + 1)
#         break

# Qn 2

# N = int(input())
# AList = list(map(int, input().split()))

# currentSum = sum(AList)
# shouldBeSum = sum([i for i in range(min(AList), max(AList) + 1)])
# print(shouldBeSum - currentSum)

# Qn 3 Brute force

# numTowns, numRoads = list(map(int, input().split()))

# roads = [[-1 for townA in range(numTowns + 1)] for townB in range(numTowns + 1)
#          ]

# for roadNum in range(numRoads):
#     townA, townB, lenC = list(map(int, input().split()))
#     roads[townA][townB] = lenC
#     roads[townB][townA] = lenC

# # print(roads)

# maxPosTotLen = 0

# townsTraversed = set()


# def maxPosTotLenTownAToTownB(townA, townB, roads, currTown, currLen=0):
#     global townsTraversed, maxPosTotLen
#     townsTraversed.add(currTown)
#     # print(townA, townB, currTown, townsTraversed, maxPosTotLen, currLen)
#     if currTown == townB:
#         maxPosTotLen = max(maxPosTotLen, currLen)
#         townsTraversed.remove(currTown)
#         return
#     for town in range(1, len(roads[currTown])):
#         if town not in townsTraversed and roads[currTown][town] != -1:
#             maxPosTotLenTownAToTownB(townA, townB, roads, town, currLen +
#                                      roads[currTown][town])
#             if town in townsTraversed:
#                 townsTraversed.remove(town)


# for townA in range(1, numTowns + 1):
#     for townB in range(townA + 1, numTowns + 1):
#         maxPosTotLenTownAToTownB(townA, townB, roads, currTown=townA)
#         if townA in townsTraversed:
#             townsTraversed.remove(townA)
# print(maxPosTotLen)

# Qn 3 Efficient

numTowns, numRoads = list(map(int, input().split()))

roads = [[-1 for _ in range(numTowns + 1)] for __ in range(
    numTowns + 1)]


for roadNum in range(numRoads):
    townA, townB, lenC = list(map(int, input().split()))
    roads[townA][townB] = lenC
    roads[townB][townA] = lenC


costOftrip = roads.copy()

for numOfRoadsInTrips in range(2, numTowns):
    print(costOftrip)
    for townA in range(1, numTowns + 1):
        for townB in range(townA + 1, numTowns + 1):
            for lastToLastTown in range(1, numTowns + 1):
                if lastToLastTown in [townA, townB] or roads[lastToLastTown][townB] == -1 or costOftrip[townA][lastToLastTown] == -1:
                    continue
                costOftrip[townA][townB] = max(costOftrip[townA]
                                               [lastToLastTown] + roads[lastToLastTown][townB], costOftrip[townA][townB])

print(max(max(costOftrip)))

# Qn 4 - Unsolved

# N = int(input())

# numOfVotersForTaka, numOfVotersForAo, numOfSeatsInDis = [0], [0], [0]

# for _ in range(N + 1):
#     x, y, z = list(map(int, input().split()))
#     numOfVotersForTaka.append(x)
#     numOfVotersForAo.append(y)
#     numOfSeatsInDis.append(z)

# additionalSeatsToWinForTaka = sum(numOfSeatsInDis) // 2 + 1 - sum([
# numOfSeatsInDis[disNum] for disNum in range(1, N + 1) if numOfVotersForTaka[
# disNum] > numOfVotersForAo[disNum]])

# if additionalSeatsToWinForTaka <= 0:
#     print(0)
# else:
#     numOfSeatsInDisOfInterest = [1]
#     voterToConvertInDisOfInterest = [1]
#     for disInd in range(1, N + 1):
#         if numOfVotersForTaka[disInd] < numOfVotersForAo[disInd]:
#             numOfSeatsInDisOfInterest.append(numOfSeatsInDis[disInd])
#             voterToConvertInDisOfInterest.append(numOfVotersForAo[disInd] -
# numOfVotersForTaka[disInd])
#     DPMapFromReqNumOfSeatsToIndexOfDisOfInterest = dict()
#     for ind in range(1, len(numOfSeatsInDisOfInterest) + 1):
#         for
