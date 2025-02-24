import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("turtle python")

turtle_instanse=turtle.Turtle()
turtle_instanse.color("black")
turtle.speed(0)

turtle_colors=["red", "green" ,"blue" ,"yellow" ,"orange", "purple"]


for i in range(10):#tekrar ediş range
 turtle_instanse.color(turtle_colors[i %6 ])#inin değerine göre sırayla renkleri alır  #yüzde işartiyle geri döndürerbiliriz
 turtle_instanse.circle(10*i)##i ile çarpıp her seferinde büyüyen daireler çiziyor
 turtle_instanse.circle(-10*i)
 turtle_instanse.left(i)



turtle.done()