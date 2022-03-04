class Syracuse:
    def __init__(self, number):
        self.number=number
        self.series=[] 

    def CalculateSeries(self):
        number=self.number
        while number > 1 :
            if number%2==0:
                self.series.append(number)
                number=int(number/2)
            else:
                self.series.append(number)
                number=number*3+1

    
    def PrintSeriesInFile(self, inputFile):
        f=open(inputFile,"w")
        self.CalculateSeries()
        for num in self.series:
            f.write(str(num)+" ")


serie= Syracuse(14)
serie.PrintSeriesInFile("test1.txt")


