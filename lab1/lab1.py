#Name: Dan-Ha Le
#Lab 1:
import math

#1: Sums all the odd number in a list:
def sumAllOdd(lst):
    tot = 0
    for x in lst:
        if x % 2 == 1:
            tot += x
    return tot

#2: Finds all prime number
def findAllPrime (lst):
    new_lst = []
    for x in lst:
        if x < 2: continue
        if x == 2: new_lst.append(x)
        if x%2 == 0: continue
        else:
            prime = True
            for i in range (3, x//2+2):
                if x%i == 0: 
                    prime = False
                    break
            if prime:
                new_lst.append(x)
    return new_lst       
        
#3: Get the largest number in a list
def findLargest (lst):
    large = lst[0]
    for x in lst:
        if large <= x:
            large = x
    return large

#4: Get the smallest number in a list
def findSmallest (lst):
    small = lst[0]
    for x in lst:
        if small >= x:
            small = x
    return small

#5: Count occurrences of a character in a string
def countStringChar (s):
    count = {}
    for i in range (len(s)):
        if s[i] not in count:
            count[s[i]] = 1
        else:
            count[s[i]] += 1
    return count

#6: Sort a list of tuples based on their last elements
def sortTuples (lst):
    n = len(lst)
    swapped = False
    for i in range(n-1):
        for j in range (n-i-1):
            if lst[j][len(lst[j])-1] > lst[j+1][len(lst[j])-1]:
                swapped = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if not swapped:
            return
    return lst

#7: Change all occurences of the first char to $ except the first char itself
def changeChar (s):
    new_s = s[0]
    for i in range (1, len(s)):
        if s[i] == s[0]:
            new_s += "$"
        else:
            new_s += s[i]
    return new_s

#8: Get a single string from two given strings, separated by a space and swap the first two characters of each string
def swapSecondChar(x, y):
    new_x = y[0] + y[1]
    new_y = x[0] + x[1]
    for i in range (2, len(x)):
        new_x += x[i]
    for i in range (2, len(y)):
        new_y += y[i]
    return new_x + " " + new_y

#9 Add "ing" to the end of strings. Other rules:
#   - If the string is not at least 3 chars, leave it unchanged
#   - If the string already ends with -ing, make it "ly"
def addIng (s):
    if len(s) < 3:
        return s
    elif s[len(s)-1] + s[len(s)-2] + s[len(s)-3] == "gni":
        return s + "ly"
    else:
        return s + "ing"

#10: Takes a list of word and returns the length of the longest one
def countLongest (lst):
    len_lst = []
    for i in range(len(lst)):
        len_lst.append(len(lst[i]))
    return findLargest(len_lst)

#11: Write a function to sort a dictionary by value (not keys) ascending and descending
#   - sortDescending == True -> descending order
# This function assumes that the values of this dictionary's keys are just a single number.
def sortDict(dict, sortDescending):
    ordered_dict = {}
    ordered_values = list(dict.values())
    bubbleSort(ordered_values)
    if sortDescending:
        ordered_values = reversed(ordered_values)
    for vals in ordered_values:
        for keys in dict:
            if dict[keys] == vals:
                ordered_dict[keys] = dict[keys] 
    return ordered_dict

#12: Concatenate dictionaries to create a new one
def concatDict (dic1, dic2, dic3):
    lst = [dic1, dic2, dic3]
    new_dict = {}
    for dic in lst:
        for key in dic:
            if key in new_dict:
                new_dict[key] += dic[key]
            else:
                new_dict[key] = dic[key]
    return new_dict


#13: Remove duplicates on a list
def removeDup (lst):
    new_lst = []
    for x in lst:
        if x in new_lst: continue
        else:
            new_lst.append(x)
    return new_lst

#14: Find the list of words that are longer than n from a given list of word
def findWord(lst, n):
    new_lst = []
    for x in lst:
        if len(x) > n:
            new_lst.append(x)
        else: continue
    return new_lst

#15: Returns true if they have at least one common number
def isCommon (lst1, lst2):
    for x in lst1:
        if x in lst2:
            return True
    return False

#16: Return three element combinations, each from an array, that equals to a target
def findCombinations(x, y, z, target):
    combos = []
    for i in range (len(x)):
        for j in range (len(y)):
            for k in range (len(z)):
                if (x[i] + y[j] + z[k] == target):
                    combos.append ([i, j, k])
    for combo in combos:
        print (x[combo[0]], y[combo[1]], z[combo[2]])

#17: Get n-th Fibonaci number:
def fib(n):
    if n <= 1:
        return n
    else: return fib(n-1) + fib(n-2)

#18: returns all sublist of a list, must have at least two elements:
def sub_lists (lst):
    lists = []
    for i in range(len(lst) + 1):
        for j in range(i):
            lists.append(lst[j: i])
    return findWord(lists, 1)

#19: Find intersection and difference of two lists
def findInterandDif (lst1, lst2):
    inter = []
    dif = []
    for i in range(len(lst1)):
        if lst1[i] in lst2: 
            inter.append(lst1[i])
        else:
            dif.append(lst1[i])
    for i in range(len(lst2)):
        if lst2[i] not in inter:
            dif.append(lst2[i])
    return [inter, dif]

def bubbleSort(lst):
    n = len(lst)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not swapped:
            return
 
def test(actual, expected):
    print (actual == expected)

def main():

    print("Problem 1: ")
    test(sumAllOdd([1, 3, 5]), 9)
    test(sumAllOdd([3, 4, 6]), 3)
    test(sumAllOdd([2, 4, 6]), 0)

    print("Problem 2: ")
    test(findAllPrime([1, 2, 3]), [2, 3])
    test(findAllPrime([521, 73, 74, 85, 14]), [521, 73])
    test(findAllPrime([-1, 0, 2, 67, 8, 3]), [2, 67, 3])

    print("Problem 3: ")
    test(findLargest([3, 4, 5, 8, 0]), 8)
    test(findLargest([10, 90, -3, 4]), 90)

    print("Problem 4: ")
    test(findSmallest([-4, 10, 4, 5]), -4)
    test(findSmallest([0, 1, 2, 3, -4, 5]), -4)

    print("Problem 5: ")
    test(countStringChar("google.com"), {"o": 3, "g": 2, ".": 1, "e": 1, "l": 1, "m": 1, "c":1})

    print("Problem 6: ")
    test(sortTuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]), [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)])
    
    print("Problem 7: ")
    test(changeChar("restart"), "resta$t")
    test(changeChar("any"), "any")

    print("Problem 8: ")
    test(swapSecondChar("abc", "xyz"), "xyc abz")
    
    print("Problem 9: ")
    test(addIng("star"), "staring")
    test(addIng("staring"), "staringly")
    test(addIng("hi"), "hi")

    print("Problem 10: ")
    test(countLongest(["hey", "hi", "longest"]), 7)
    
    print("Problem 11: ")
    test(sortDict({"two":2, "one": 1, "three": 3, "four": 3, "five": 5}, False), {"one": 1, "two":2, "three":3, "four":3, "five": 5})

    print("Problem 12: ")
    test(concatDict({1:10, 2: 20}, {2:30, 4:40}, {5:50, 4:60}), {1:10, 2:50, 4:100, 5:50})

    print("Problem 13: ")
    test(removeDup([1, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    print ("Problem 14: ")
    test(findWord(["is", "babe", "hello", "tan", "yuh"], 3), ["babe", "hello"])

    print("Problem 15: ")
    test(isCommon([],[]), False)
    test(isCommon([1, 2, 3], [3, 4, 5]), True)

    print ("Problem 17: ")
    test(fib(3), 2)
    test(fib(6), 8)
    
    print ("Problem 18: ")
    test(sub_lists([1, 2, 3, 4]), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 3, 4], [2, 3, 4]])
    print("Wrong order but the same sublists")

    print("Problem 19: ")
    test(findInterandDif([1, 2, 3],[2, 4, 5]), [[2],[1, 3, 4, 5]])
if __name__ == '__main__':
    main()


    

        
    



 

                

        


        
