class Car:
    #constuctor


    def __init__(self,brand,speed =0):
        self.brand=brand
        self.speed=speed
        #local variable of a class coming as an argument


    def accelerate(self):
        self.speed +=30

    def get_speed(self):
        return self.speed
    
