"""
John has collected various rocks. Each rock has various minerals embeded in it. Each type of mineral is designated by a lowercase letter in the range . There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs at least once in each of the rocks in John's collection.

Given a list of minerals embedded in each of John's rocks, display the number of types of gemstones he has in his collection.

For example, the array of mineral composition strings . The minerals  and  appear in each composite, so there are  gemstones.

Function Description

Complete the gemstones function in the editor below. It should return an integer representing the number of gemstones found in the list of rocks.

gemstones has the following parameter(s):

arr: an array of strings
Input Format

The first line consists of an integer , the size of .
Each of the next  lines contains a string  where each letter represents an occurence of a mineral in the current rock.

Constraints


 | arr[i] | 
Each composition  consists of only lower-case Latin letters ('a'-'z').

Output Format

Print the number of types of gemstones in John's collection. If there are none, print .

Sample Input

3
abcdde
baccd
eeabg
Sample Output

2
Explanation

Only  and  are gemstones because they are the only types that occur in every rock.
"""

rocks = [set(input()) for _ in range(int(input()))]
gems = set.intersection(*rocks)
print(len(gems))
