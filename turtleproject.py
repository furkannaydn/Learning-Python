import turtle

drawing_board=turtle.Screen()#screen,ekranı oluşturur
drawing_board.bgcolor("blue")#arka planı mavi yaptık
drawing_board.title("python turtle")

'''
turtle_instance=turtle.Turtle()
turtle_instance.forward(100)#ileri 
turtle_instance_2=turtle.Turtle()
turtle_instance_2.left(45)#sola döndürdük
turtle_instance_2.forward(100)
turtle.done()
'''
#kare yapımı
'''
turtle_instance=turtle.Turtle()
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
'''

'''
turtle_instance=turtle.Turtle()
for i in range(4):#döngüyle yapmak
    turtle_instance.forward(200)
    turtle_instance.left(90)
'''

#yıldız yapımı
'''
turtle_instance=turtle.Turtle()
for i in range(5):#döngüyle yapmak
    turtle_instance.forward(100)
    turtle_instance.left(144)

turtle.done()
'''

#polygon yapımı 

'''
turtle_instance=turtle.Turtle()

num_sides=6#kenar
angale = 360.0 / num_sides#açı
side_length=100#ne kadar ileri gittiği


for i in range(num_sides):#döngüyle yapmak
    turtle_instance.forward(side_length)
    turtle_instance.left(angale)

turtle.done()
'''




