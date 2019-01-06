class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        corners = {}
        corners["north-west"] = [self.south + self.width_NS, self.west]
        corners["north-east"] = [self.south + self.width_NS, self.west + self.width_WE]
        corners["south-west"] = [self.south, self.west]
        corners["south-east"] = [self.south, self.west + self.width_WE]
        return corners

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return "Building({south}, {west}, {width_we}, {width_ns}, {height})".format(
            south=self.south,
            west=self.west,
            width_we=self.width_WE,
            width_ns=self.width_NS,
            height=self.height)
