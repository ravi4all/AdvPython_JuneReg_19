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

class CarV2():
    def __init__(self):
        self.automatic = True

    def updatedFeatures(self):
        print("Automatic : {}".format(self.automatic))

class CarV3(CarV1,CarV2):

    def __init__(self,wheels,speed,avg,hybrid):
        super().__init__()
        CarV2.__init__(self)
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

car = CarV3('Alloy',400,15,True)
car.updatedFeatures()