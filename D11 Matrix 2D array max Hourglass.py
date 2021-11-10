# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# Sample Output

# 19

# Explanation

# contains the following hourglasses:

# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0

# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0

# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0

# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0
# The hourglass with the maximum sum (19) is:

# 2 4 4
#   2
# 1 2 4
def matrix(row,col):
    ret = []
    for i in range(row):
        l = []
        for j in range(col):
            l.append(int(input()))
        m.append(l)
    HourGlass = []
    for i in range(row):
        for j in range(col):
            if ((j==0)or(j==col-1)or(i==0)or(i==row-1)):
                continue
            else:  
                Sum = (ret[i][j])+(ret[i-1][j-1])+(ret[i-1][j])+(ret[i-1][j+1])+(ret[i+1][j-1])+(ret[i+1][j])+(ret[i+1][j+1])
                HourGlass.append(Sum)
    return (max(HourGlass))
    
def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of column:"))
    
    ret = matrix(row,col)
    print(ret)
if __name__ == "__main__":
    main()
