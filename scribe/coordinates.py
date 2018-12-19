

class Coordinates:
    """
    A 2D coordinate system defined by an origin at the "top left" 
    with only positive values less than 1 allowed. (e.g. x=1 is limit
    to the "right" and y=1 is the limit "down").
    """

    def __init__(self, x, y):
        self.validate_coordinates(x, y)
        self.x = x
        self.y = y

    def validate_coordinates(self, x, y):
        if x > 1 or x < 0 or y > 1 or y < 0:
            raise Exception('Coordinate values must be between 0 and 1')
