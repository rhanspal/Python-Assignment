'''Exercise #2:  An Aircraft Object'''

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

print("# Exercise 2")
instance = Aircraft()
print("Initial X-Coord:", instance.x)
print("Initial X-Coord:", instance.y)

instance.move_right()
instance.move_right()
instance.move_up()
instance.move_right()
instance.move_left()
instance.move_up()
instance.move_up()
instance.move_down()
instance.move_up()
instance.move_down()
instance.move_up()
print("Final X-Coord:", instance.x)
print("Final X-Coord:", instance.y)
