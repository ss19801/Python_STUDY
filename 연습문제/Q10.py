class Calculator:
    def __init__(self,numlist):
        self.numlist=numlist

    def sum(self):
        total=0
        for num in self.numlist:
            total+=num
        return total
    
    def avg(self):
        average=self.sum()/len(self.numlist)
        return average
    
cal1=Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())
