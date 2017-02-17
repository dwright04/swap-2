################################################################
# Parent class for all agents


class Agent:
    """ Agent to represent a user or subject
    """
    
    def __init__(self, id, probability):
        self.id = id
        self.probability = probability
        
        
    def getID(self):
        return self.id