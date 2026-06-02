
# define constant speeds
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

# create private attributes for speed, radius, color, and status
    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = on
        
# create getter methods to read values
# create setter methods to change values