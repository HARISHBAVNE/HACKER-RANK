class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        self.maximumDifference = 0
        for i in range(len(self.__elements)):
            for j in range(i+1,len(self.__elements)):
                sub = a[j]-a[i]
                if sub < 0:
                    sub = -(sub)
                if (sub > self.maximumDifference):
                    self.maximumDifference = sub
    
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
