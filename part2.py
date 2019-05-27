"""
 1. Time O(N) and space O(N)

 2. Time O(N) and space O(N)
"""

def allElementInHashT(str):
    dictStr = dict()
    for element in str:
        if element not in dictStr:
            dictStr[element] = 1
        else:
            dictStr[element] += 1
    return dictStr

def isStringPermutation(s1,  s2):
    if len(s1) != len(s2):
        return False

    #since both string length is not same so if one string length is 0, then other should be 0
    if len(s1) == 0:
        return True

    dictStr2 = allElementInHashT(s2)

    for char in s1:
        if char not in dictStr2:
            return False
        else:
            dictStr2[char] -= 1
            # if dict value become 0, then delete the that key value pair
            if dictStr2[char] == 0:
                del dictStr2[char]
    return True


def pairsThatEqualSum(array, targetSum):

    #using set so there will be no duplicate tuple output
    output = set()

    if len(array) == 0 or targetSum == 0:
        return output

    arrHash = allElementInHashT(array)
    for element in array:
        numToFind = targetSum - element
        if numToFind in arrHash:
            #input = [1,2,3,4], sum = 2, output = [(1,1)] which is wrong so
            if numToFind == element and arrHash[element] == 1:
                continue

            #since (0, 3) and (3, 0) are consider to be same
            if (numToFind, element) in output:
                continue

            output.add((element, numToFind))
    return output



# unit Test for isStringPermutation
print("-----------Unit Test for isStringPermutation(s1,  s2)---------------")
print('Both empty String: {}'.format(isStringPermutation("","")))
print("(Kind), (niKd): {}".format(isStringPermutation("Kind", "niKd")))
print("(Johhny), (hnJoyh): {}".format(isStringPermutation("Johhny", "hnJoyh")))
print("(World), (Worrd): {}".format(isStringPermutation("World", "Worrd")))
print("( ), (Team): {}".format(isStringPermutation("", "Team")))

#unit Test for pairsThatEqualSum(array, targetSum)
print("-----------Unit Test for pairsThatEqualSum(array, targetSum)---------------")
print("(array = [], targetSum = 1):   {}".format(pairsThatEqualSum([], 1)))
print("(array = [1,4, 6, 3], targetSum =  2):   {}".format(pairsThatEqualSum([1,11,6,3,4,7,14,19,9], 2)))
print("(array = [0,1,40, 100, 5, 40, 95, 12, 40, 45, 1, 0], targetSum = 5):   {}".format(pairsThatEqualSum([0,40, 100, 5, 40, 95, 12, 40, 45, 0], 5)))
print("(array = [3,8,2,9,10,5,7,1,0], targetSum = 10):   {}".format(pairsThatEqualSum([3,8,2,9,10,5,7,1,0], 10)))
print("(array = [3,8,2,9,10,5,7,1,0,3], targetSum = 0):   {}".format(pairsThatEqualSum([3,8,2,9,10,5,7,1,0,3], 0)))
print("(array = [2,2,2,2,2,2,2,2], targetSum = 4):   {}".format(pairsThatEqualSum([2,2,2,2,2,2,2,2], 4)))




