#Cole McLean CSCI 161 Thursday Lab
class Robot:
    def __init__(self, weight, max_speed, number_of_batteries):
        self.weight = weight
        self.max_speed = max_speed
        self.number_of_batteries = number_of_batteries
        self.speed = 0
        self.direction = "Stopped"

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed

    def set_number_of_batteries(self, number_of_batteries):
        self.number_of_batteries = number_of_batteries

    def get_number_of_batteries(self):
        return self.number_of_batteries

    def drive(self, speed, direction):
        if speed <= self.max_speed:
            self.speed = speed
            self.direction = direction
            print(f"Robot is now driving at {speed} km/h in the {direction} direction.")
        else:
            print(f"Error Speed {speed} km/h exceeds maximum speed {self.max_speed} km/h of the robot")


class KillerRobot(Robot):
    def __init__(self, weight, max_speed, number_of_batteries, weapon, armor):
        super().__init__(weight, max_speed, number_of_batteries)
        self.weapon = weapon
        self.armor = armor
        self.target = None

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_weapon(self):
        return self.weapon

    def set_armor(self, armor):
        self.armor = armor

    def get_armor(self):
        return self.armor

    def attack(self, speed, direction, range, target):
        super().drive(speed, direction)
        self.target = target
        print(f"KillerRobot is attacking {target} at {speed} km/h in the {direction} direction within range of {range} meters.")


# Create instances of both Robot and KillerRobot classes
robot = Robot(100, 50, 2)
killer_robot = KillerRobot(150, 70, 3, "Laser", "Titanium")

# Set attributes for both instances
robot.set_weight(120)
killer_robot.set_armor("Steel")

# Print out attributes
print("Robot Attributes:")
print("Weight:", robot.get_weight())
print("Max Speed:", robot.get_max_speed())
print("Number of Batteries:", robot.get_number_of_batteries())

print("\nKillerRobot Attributes:")
print("Weight:", killer_robot.get_weight())
print("Max Speed:", killer_robot.get_max_speed())
print("Number of Batteries:", killer_robot.get_number_of_batteries())
print("Weapon:", killer_robot.get_weapon())
print("Armor:", killer_robot.get_armor())

# Call methods
robot.drive(40, "North")
killer_robot.attack(60, "East", 100, "Enemy Base")
