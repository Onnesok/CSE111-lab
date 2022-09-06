class a:
    temp = 6
    def __init__(self):
        self.temp += 1
        print(self.temp)

class b(a):
    def __init__(self) -> None:
        super().__init__()
        a.temp += 3
        print(self.temp, a.temp)



calling = a()
bb = b()
calling = a()