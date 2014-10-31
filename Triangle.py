class Triangle:

    def __init__(self, args):
        self.lado = args[0:]

    def istriangle(self):
        a = self.lado[0]
        b = self.lado[1]
        c = self.lado[2]

        if(a > 200 or b > 200 or c > 200):
            return "NotATriangle"
        elif a > (b + c) or b > (a + c) or c > (a + b):
            return "NotATriangle"
        elif a == b and b == c:
            return "Equilateral"
        elif a != b and b != c and a != c:
            return "Scalene"
        else:
            return "Isosceles"
