import turtle
import random

# Screen settings (Ekran ayarları)
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

# Font settings (Font ayarı)
FONT = ('Arial', 20, 'normal')

# Score and game state variables (Skor ve oyun durumu değişkenleri)
score = 0
game_over = False

# List to store turtles (Tüm kaplumbağaları saklamak için liste)
turtle_list = []




# Turtle for displaying score (Skoru göstermek için turtle)
score_turtle = turtle.Turtle()

# Turtle for countdown timer (Geri sayım göstergesi için turtle)
countdown_turtle = turtle.Turtle()

# Function to set up the score display (Skor gösterme fonksiyonu)
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = screen.window_height() / 2  # Position the score display at the top (Skorun ekranın üst kısmına konumlanması)
    y = top_height * 0.90
    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

# Function to create a turtle (Kaplumbağa oluşturma fonksiyonu)
def make_turtle(x, y):
    t = turtle.Turtle()
    
    # Function to increase score when clicked (Tıklanınca skoru artıran fonksiyon)
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)
    
    t.onclick(handle_click)  # Trigger function when clicked (Kaplumbağaya tıklanınca çalışacak)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)  # Add turtle to list (Kaplumbağayı listeye ekle)

# Coordinate lists (Koordinat listeleri)
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10, -20]
grid_size = 12

# Function to set up turtles (Kaplumbağaları oluşturma fonksiyonu)
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

# Function to hide all turtles (Kaplumbağaları gizleme fonksiyonu)
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

# Function to show a random turtle repeatedly (Rastgele bir kaplumbağayı gösteren fonksiyon)
def show_turtles_randomly():
    if not game_over:
        hide_turtles()  # Hide all turtles first (Önce tüm kaplumbağaları gizle)
        random.choice(turtle_list).showturtle()  # Show a random turtle (Rastgele birini göster)
        screen.ontimer(show_turtles_randomly, 700)  # Repeat after 700ms (700ms sonra tekrar çağır)

# Function to start countdown timer (Geri sayımı başlatan fonksiyon)
def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()
    top_height = screen.window_height() / 2  # Position countdown display (Geri sayımın konumu)
    y = top_height * 0.90
    countdown_turtle.setposition(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)  # Call itself after 1 second (1 saniye sonra kendini tekrar çağır)
    else:
        game_over = True
        hide_turtles()
        countdown_turtle.clear()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)



# Function to start the game (Oyunu başlatan fonksiyon)
def start_game_up():
    turtle.tracer(0)  # Disable animation for speed (Çizimleri hızlandırmak için animasyonu kapat)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()  # Start showing turtles randomly (Kaplumbağaları rastgele göster)
    countdown(10)  # Start countdown from 10 seconds (10 saniyelik geri sayım başlat)
    turtle.tracer(1)  # Enable animation again (Animasyonu tekrar aç)

# Start the game (Oyunu başlat)
start_game_up()
turtle.mainloop()  # Keep screen open (Ekranın açık kalmasını sağlar)