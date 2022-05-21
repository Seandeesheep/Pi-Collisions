# 21/05/22
"""Welcome to one of the slowest ways of computing pi"""
n = 7
#^ this n refers to the amount of digits of pi


import time
start = time.process_time()


class Pi:
    def __init__(self, n):
        self.M = float(100 ** (n - 1))
        self.n = 0
        self.Vn = 1
        self.vn = float(0)

    def collide(self):
        self.n += 1
        if self.n == 1:
            self.vn = (2 / (self.M + 1)) * self.M
            self.Vn = ((self.M - 1) / (self.M + 1))
        else:
            new_Vn = (1 / (self.M + 1)) * ((self.M - 1) * self.Vn - 2 * self.vn)
            new_vn = (1 / (self.M + 1)) * ((self.M - 1) * self.vn + 2 * self.M * self.Vn)
            self.Vn = new_Vn
            self.vn = new_vn

    def total_collision(self):
        _n = self.n * 2
        if self.vn <= 0:
            return _n - 1
        else:
            return _n


data = Pi(n)
collision = True
while collision:
    if data.Vn < 0 and abs(data.Vn) > abs(data.vn):
        print(f"After {data.n} collisions:\nBody M has velocity {data.Vn}\nBody m has velocity {data.vn}")
        print("They can no longer collide")
        print(f"Total collisions: {data.total_collision()}")
        collision = False
    else:
        print(f"After {data.n} collisions:\nBody M has velocity {data.Vn}\nBody m has velocity {data.vn}")
        data.collide()

print(f"It takes {time.process_time() - start}s for the system to compute {n} digits of pi... and print out a heck ton of lines of strings")
