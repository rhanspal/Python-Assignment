class Aircraft:
    x=y = 0
    acceleration = 1

    def move_left(self):
        print("Moved Left..")
        self.x,self.y = self.decrement(self.x,self.y)
        # print(self.x,self.y)

    def move_right(self):
        print("Moved Right..")
        self.x,self.y = self.increment(self.x,self.y)
        # print(self.x,self.y)

    def move_up(self):
        self.x,self.y = self.increment(self.x,self.y)
        print("Moved Up..")

    def move_down(self):
        print("Moved Down..")
        self.x,self.y = self.decrement(self.x,self.y)

    def increment(self,x,y):
        x=x+1
        y=y+1
        return x,y

    def decrement(self,x,y):
        x=x-1
        y=y-1
        return x,y

print("# Exercise 3")
instance_1 = Aircraft()
print("Initial X-Coord:", instance_1.x)
print("Initial X-Coord:", instance_1.y)

instance_2 = Aircraft()
print("Initial X-Coord:", instance_2.x)
print("Initial X-Coord:", instance_2.y)

instance_3 = Aircraft()
print("Initial X-Coord:", instance_3.x)
print("Initial X-Coord:", instance_3.y)
