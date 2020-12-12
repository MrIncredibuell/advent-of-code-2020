

data = [(x[0], int(x[1:])) for x in open('data.txt').read().split('\n')]

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0
    
    def move(self, action, value):
        if action == 'N':
            self.y += value
        elif action == 'S':
            self.y -= value
        elif action == 'E':
            self.x += value
        elif action == 'W':
            self.x -= value
        elif action == 'L':
            self.direction = (self.direction + value) % 360
        elif action == 'R':
            self.direction = (self.direction - value) % 360
        elif action == 'F':
            if self.direction == 0:
                self.x += value
            elif self.direction == 90:
                self.y += value
            elif self.direction == 180:
                self.x -= value
            elif self.direction == 270:
                self.y -= value


class WaypointShip:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1
    
    def move(self, action, value):
        if action == 'N':
            self.waypoint_y += value
        elif action == 'S':
            self.waypoint_y -= value
        elif action == 'E':
            self.waypoint_x += value
        elif action == 'W':
            self.waypoint_x -= value
        elif action == 'L':
            while value > 0:
                self.waypoint_x, self.waypoint_y = (-1 * self.waypoint_y, self.waypoint_x)
                value -= 90
        elif action == 'R':
            while value > 0:
                self.waypoint_x, self.waypoint_y = (self.waypoint_y, -1 * self.waypoint_x)
                value -= 90
        elif action == 'F':
            self.x += self.waypoint_x * value
            self.y += self.waypoint_y * value
            

def part1(data):
    s = Ship()
    for a, v in data:
        s.move(a,v)
    return abs(s.x) + abs(s.y)
        

def part2(data):
    s = WaypointShip()
    for a, v in data:
        s.move(a,v)
    return abs(s.x) + abs(s.y)

print(part1(data))
print(part2(data))