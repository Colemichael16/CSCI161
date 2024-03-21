#Cole McLean CSCI 161 Midterm #5 MWF class
class Aircraft:
    def __init__(self, tail_number, latitude, longitude, altitude, heading, speed):
        self.attributes = {
            "tail_number": tail_number,
            "latitude": latitude,
            "longitude": longitude,
            "altitude": altitude,
            "heading": heading,
            "speed": speed
        }

    def print_plane(self):
        for attribute, value in self.attributes.items():
            print(f"{attribute}: {value}")


def main():
    airplanes = []
    for i in range(3):
        tail_number = (input("Enter Tail Number "))
        latitude = (input("Enter Latitude "))
        longitude = (input("Enter Longitude "))
        altitude = (input("Enter Altitude "))
        heading = (input("Enter Heading "))
        speed = (input("Enter Speed "))

        plane = Aircraft(tail_number, latitude, longitude, altitude, heading, speed, )
        airplanes.append(plane)

    for plane in airplanes:
        print("\nPlane Info ")
        plane.print_plane()


main()
