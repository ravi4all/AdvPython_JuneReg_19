class CarV1():

    def __init__(self):
        self.brand = "Tata"
        self.sedan = True
        self.wheels = 'Simple'
        self.speed = 200
        self.avg = 20
        self.hybrid = False

    def showDetails(self):
        print("Welcome to {}".format(self.brand))
        print("Features are : ")
        print("Speed : {}, Avg : {}".format(self.speed, self.avg))
        print("Wheels : {}".format(self.wheels))
        print("Sedan : {}, Hybrid : {}".format(self.sedan, self.hybrid))

class CarV2(CarV1):
    def __init__(self):
        super().__init__()
        self.automatic = True

    def updatedFeatures(self,avg,speed):
        self.avg = avg
        self.speed = speed
        print("Updated Features are :")
        print("Speed : {}, Avg : {}".format(self.speed, self.avg))
        print("Automatic : {}".format(self.automatic))

# obj = CarV2()
# obj.showDetails()
# obj.updatedFeatures(18,300)

class CarV3(CarV2):

    def __init__(self,sedan,wheels,speed,avg,hybrid):
        super().__init__()

        self.sedan = sedan
        self.wheels = wheels
        self.speed = speed
        self.avg = avg
        self.hybrid = hybrid

    def updatedFeatures(self):
        print("Updated Features are : ")
        print("Speed : {}, Avg : {}".format(self.speed, self.avg))
        print("Wheels : {}".format(self.wheels))
        print("Sedan : {}, Hybrid : {}".format(self.sedan, self.hybrid))
        print("Automatic : {}".format(self.automatic))

car = CarV3(False,'Alloy',400,15,True)
car.updatedFeatures()