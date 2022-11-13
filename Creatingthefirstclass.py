class Phone:#first letter of class should be capital
    def make_call(self):
        print("Making phone call")
    def play_game(self):
        print("Playing Game")
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
p1=Phone()
p1.set_color('Blue')
p1.set_cost(5000)
print(p1.show_color())
print(p1.show_cost())
p1.play_game()