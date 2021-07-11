class edge:
    S = None
    D = None

    def __init__(self, S, D):
        self.S = S
        self.D = D
        edge.S = S
        edge.D = D


    def __eq__(self, other):
        if isinstance(other, edge):
            return ((self.S == other.S) and (self.D == other.D))
        else:
            return False

    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((edge.S, edge.D))

    def __lt__(self, other):
        return self.S < other.S and self.S < other.D