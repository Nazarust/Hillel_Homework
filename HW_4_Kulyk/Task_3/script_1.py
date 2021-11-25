

# Реалізуйте клас вектора. Перегрузіть оператор + і * таким чином, щоб
# при додаванні двох векторів, утворювався новий вектор, координатами
# якого буде сума відповідних координат. При множені двох векторів,
# результатом буде число яке рахується по формулі – сума добуктів
# відповідних координат. При додаванні або мнодені вектора на число
# (константу), всі координати додаються або множаться на дане число
# відповідно.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Vector [{self.x}, {self.y}, {self.z}]'

    def __add__(self, other):
        if type(other) in [int, float]:
            return Vector(self.x + other, self.y + other, self.z + other)
        else:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
            return x + y + z



v1 = Vector(3, 5, 6)
v2 = Vector(2, 5, 7)
v3 = Vector(3, 5, 4)
print(v1, v2, v3)
print(v1 + v2)
print(v1 + 3)
print(v1 * v2)
print(v1 * 2)


