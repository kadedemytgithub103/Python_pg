class Operetion:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self) -> int:
        res = 0
        for num in range(self.x,self.y + 1):
            res += num

        return res

class Main:

    def execute(self) -> None:
        calc_exec = Operetion(100,200)
        total = calc_exec.sum()
        print("{}から{}の合計は{}です。".format(calc_exec.x,calc_exec.y,total))

main = Main()
main.execute()