#Cole McLean CSCI 161 Thursday Lab
class Robot:
    def set_weight(self,weight):
        self.weight=weight
    def get_weight(self):
        return self.weight
    def set_max_speed(self,max_speed):

    def get_max_speed(self):
    def set_number_of_batteries(self,number_of_batteries):
    def get_number_of_batteries(self):
    def __innit__(self,weight,max_speed,number_of_batteries,weapon,armor):
        super().__init__(weight,max_speed,number_of_batteries)
    def drive(self,speed, direction):
        if speed <= self.max_speed:
            self.speed = speed
            self.direction = direction
            print (f"Robot is driving at {speed} km/h in the {direction} direction")

class killerRobot:
    def attack(self,speed):
