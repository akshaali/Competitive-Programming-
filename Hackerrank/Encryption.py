
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    n = len(s)
    print(s[2:])
    col = math.ceil(math.sqrt(n))
    row = math.floor(math.sqrt(n))
    arr = []
    i = 0
    while(i<n):
        if n - i >= col:
            arr.append(s[i:i+col])
            #print(arr)
            i += col 
        else:
            arr.append(s[i:])
            i = n
    print(arr)
    s = ""
    k = 0
    for i in range(len(arr[k])):
        for j in range(len(arr)):
            if i < len(arr[j]):
                s += arr[j][i]
            else:
                break
            print(s , i, j)
        s +=" "
        k +=1 
    return(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()





    """
        string s;
    cin >> s;
    auto n = s.size();
    int row = round(sqrt(n));
    int column;
    if (row >= sqrt(n)) column = row; else column = row + 1;
    for(int j=0;j<column;++j) {
        for(int i=j; i<n;i+=column)cout << s[i];
        cout << ' ';
    }
    return 0;
}
    """

