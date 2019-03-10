import turtle, os


class Shape(turtle.Turtle):
    def __init__(self, shape, color, goto):
        turtle.Turtle.__init__(self)
        self.shape(shape)
        self.color(color)
        self.penup()
        self.goto(goto, 0)


class Player(Shape):
    def __init__(self, shape, color, goto, swid, slen):
        Shape.__init__(self, shape, color, goto)
        self.shapesize(swid, slen)

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)


class Ball(Shape):
    def __init__(self, shape, color, goto):
        Shape.__init__(self, shape, color, goto)
        self.dx = 0.1
        self.dy = 0.1

    def update(self, play_a, play_b):
        self.collision(play_a, play_b)
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def collision(self, play_a, play_b):
        if self.ycor() > 290:
            ball.sety(290)
            self.dy *= -1
        elif self.ycor() < -290:
            ball.sety(-290)
            self.dy *= -1

        if self.xcor() < -340 and self.diff(play_a):
            self.dx *= -1
        elif self.xcor() > 340 and self.diff(play_b):
            self.dx *= -1

    def diff(self, player):
        return self.ycor() < player.ycor() + 60 and self.ycor() > player.ycor() - 60


class Score(Shape):
    def __init__(self, shape, color, goto):
        Shape.__init__(self, shape, color, goto)
        self.goto(0, goto)
        self.score_a = 0
        self.score_b = 0
        self.hideturtle()
        self.draw()

    def update(self, ball):
        if ball.xcor() > 350:
            self.score_a += 1
            self.clear()
            self.draw()
            ball.goto(0, 0)
        elif ball.xcor() < -350:
            self.score_b += 1
            self.clear()
            self.draw()
            ball.goto(0, 0)

    def draw(self):
        self.write(
            "Jogador A: {}   Jogador B: {}".format(self.score_a, self.score_b),
            font=("Arial", 22, "normal"),
            align="center",
        )


play_a = Player("square", "white", -350, 6, 0.7)
play_b = Player("square", "white", 350, 6, 0.7)
ball = Ball("square", "white", 0)
score = Score("square", "white", 260)

# Main Window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Events
wn.listen()
wn.onkeypress(play_b.up, "Up")
wn.onkeypress(play_b.down, "Down")
wn.onkeypress(play_a.up, "w")
wn.onkeypress(play_a.down, "s")

while True:
    wn.update()
    ball.update(play_a, play_b)
    score.update(ball)
