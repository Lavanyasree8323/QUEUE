class Que:
    def __init__(self):
        self.Q=[]
    def isempty(self):
        return self.Q==[]
    def add(self,element):
        self.Q.append(element)
    def delete(self):
        if self.isempty():
            return -1
        else:
            return self.Q.pop(0)
    def search(self,element):
        if self.isempty():
            return -1
        else:
            try:
                n=self.Q.index(element)
                return -1
            except ValueError:
                return -3
    def display(self):
        return self.Q
            