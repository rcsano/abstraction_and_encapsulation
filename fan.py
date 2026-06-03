
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
        def get_speed(self): return self.speed
        def get_radius(self): return self.radius
        def get_color(self): return self.color
        def is_on(self): return self.on

# create setter methods to change values
        def set_speed(self, speed): self.speed = speed
        def set_radius(self, radius): self.radius = radius
        def set_color(self, color): self.color = color
        def set_on(self, on): self.on = on
