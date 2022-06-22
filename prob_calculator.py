import copy
import random

# Consider using the modules imported above.
# dynamic class attributes seen from from https://medium.com/@nschairer/python-dynamic-class-attributes-24a89df8da7d

class Bolas:
    def __init__(self, color, cantidad):
        self.color = color
        self.cantidad = cantidad
    
    def __repr__(self):
        return str(self.cantidad)

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for color, valor in kwargs.items():
            setattr(self, color, Bolas(color, valor))
            for i in range(valor):
                self.contents.append(color)

    def draw(self, cantidad):
        draw_list = list()
        if cantidad < len(self.contents):
            for i in range(cantidad):
                sel = random.choice(self.contents)
                draw_list.append(sel)
                self.contents.remove(sel)
            return draw_list
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    casos_favorables = 0
    for i in range(num_experiments):
        bolsa = copy.deepcopy(hat)
        extracted_balls = bolsa.draw(num_balls_drawn)
        bools_list = list()
        for color, cantidad in expected_balls.items():
            if extracted_balls.count(color) < cantidad:
                bools_list.append(0)
            else:
                bools_list.append(1)
        if bools_list.count(0) == 0:
            casos_favorables += 1
    return (casos_favorables / num_experiments)







# hat1 = Hat(yellow=3, blue=2, green=6)
# print(hat1.green)
# print(hat1.contents)

# hat = Hat(black=6, red=4, green=3)
# probability = experiment(hat=hat,
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=5,
#                   num_experiments=2000)

# print(probability*100.0)

# hat = Hat(blue=3,red=2,green=6)
# probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=5, num_experiments=1000)
# print(probability)