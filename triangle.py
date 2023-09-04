# Семинар 13. Исключения по треугольнику

class InvalidTriangleError(Exception):
    def __init__(self, sides):
        self.sides = sides

    def __str__(self):
        return f"InvalidTriangleError: Треугольник с сторонами {self.sides} не может существовать."

class EquilateralTriangleError(Exception):
    def __str__(self):
        return "EquilateralTriangleError: Треугольник равносторонний."

class IsoscelesTriangleError(Exception):
    def __str__(self):
        return "IsoscelesTriangleError: Треугольник равнобедренный."

class ScaleneTriangleError(Exception):
    def __str__(self):
        return "ScaleneTriangleError: Треугольник является скалярным."
    
class Triangle:
    def __init__(self):
        self.a = float(input("Введите длину стороны a: "))
        self.b = float(input("Введите длину стороны b: "))
        self.c = float(input("Введите длину стороны c: "))

    def check_triangle(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            print("Треугольник с такими сторонами существует.")
            self.check_triangle_type()
        else:
            raise InvalidTriangleError([self.a, self.b, self.c])

    def check_triangle_type(self):
        if self.a == self.b and self.b == self.c:
            raise EquilateralTriangleError()
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            raise IsoscelesTriangleError()
        else:
            raise ScaleneTriangleError()

try:
    triangle = Triangle()
    triangle.check_triangle()
except InvalidTriangleError as e:
    print(e)
except EquilateralTriangleError as e:
    print(e)
except IsoscelesTriangleError as e:
    print(e)
except ScaleneTriangleError as e:
    print(e)