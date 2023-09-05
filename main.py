class name:
    x=0
    name=""
    def __init__(self,z):
        self.name=z
        print("hi",z)
n=name("Deepak")
class Football(name):
    def pts(self):
        print("Scores",self.name)
p=Football()
p.pts()
