from REC2 import Rectangle_2, Square, Circle

#создаем 2 прямоугольника
rect_1 = Rectangle_2(6, 5)
rect_2 = Rectangle_2(8, 5)
#возвращаем ответ
print("Прямоугольник 1 = ", rect_1.get_area())
print("Прямоугольник 2 = ", rect_2.get_area())

#создаем 2 квадрата
sq_1 = Square(5)
sq_2 = Square(8)
#возвращаем ответ
print("Квадрат 1 = ", sq_1.get_square())
print("Квадрат 2 = ", sq_2.get_square())

#создаем 2 круга
cr_1 = Circle(3)
cr_2 = Circle(9)
#возвращаем ответ
print("Круг 1 = ", cr_1.get_circle())
print("Круг 2 = ", cr_2.get_circle())



figures = [rect_1, rect_2, sq_1, sq_2, cr_1, cr_2]
for figure in figures:
    if isinstance(figure, Square):
        print(f"Квадрат = {figure.get_square()}")
    elif isinstance(figure, Rectangle_2):
        print(f"Прямоугольник = {figure.get_area()}")
    else :
        print(f"Круг = {figure.get_circle()}")

