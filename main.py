import play  #Loading the play modulue Library
import random  #Loading the play modulue Library

w = 300  #Defining global variable for horizontal size of the court
h = 400  #Defining global variable for vertial size of the court
halfw = w / 2  #defining global variable for horizontal size of the court
halfh = h / 2  #defining global variable for vertial size of the court
score = 0  #Defining global variable for score
speed = 3  #Defining global variable for speed of ball


@play.when_program_starts  #This creates a keyframe to start the game function as soon as you press run
def backGround():
  play.set_backdrop((108, 147, 92))  #This sets the background to a color


court = play.new_box(
    color=((198, 237, 44)),  #Set the court color
    x=0,  # x coordinate of court
    y=0,  # x coordinate of court
    width=w,  #Use global variable to populate local variable
    height=h,  #Use global variable to populate local variable
)

ball = play.new_circle(
    color="blue",
    radius=10,
    x=0,
    y=halfh - 30,
    angle=random.randint(210, 330),
)

paddle = play.new_box(
    color=((100, 6, 0)),  #Set the color of the paddle
    width=50,  #Use global variable to populate local variable
    height=10,  #Use global variable to populate local variable
    x=0,
    y=-halfh + 10,
)

# creating and initializing a variable for the text of the score
# and initailizing it with a built in function new text from play module
score_text = play.new_text(
    words=('Score:' + str(score)),  #Set the score to a string
    x=0,
    y=halfh + 15,
    font=None,
    color="white",
)


@play.repeat_forever  #key frame to do the following code as long as the program is running
def ball():  #define the function
  global score  #calling for the global variable score
  paddle.x = play.mouse.x  #DOT notation to recall the X parameter of the paddle and reassign value to match mouse x coordinates
  if(play.mouse.x < -halfw + paddle.width / 2):  #if statement to set the paddle to the edges of the court and to ensure the paddle is not moving off the court.
    paddle.x = -halfw + paddle.width / 2

  if(play.mouse.x > halfw - paddle.width / 2):
    paddle.x = halfw - paddle.width / 2
    
  ball.move(3)#bounce off the screen

  if (ball.y + ball.radius > halfh):
    ball.angle = 360 - ball.angle  #bounce of the screen

  if (ball.y - ball.radius < -halfh):
    ball.angle = 360 - ball.angle  #bounce of the screen)
    score -= 1
  #bounce off left/right: 180 - angle
  # right wall
  if (ball.x + ball.radius > halfw):
    ball.angle = 180 - ball.angle  #bounce of the screen

  # left wall
  if (ball.x - ball.radius < -halfw):
    ball.angle = 180 - ball.angle  #bounce of the screen
    #make sure it bounce as if it has hit the bottom, and give it a little change of trajectory

  if (ball.is_touching(paddle)):
    ball.angle = 360 - ball.angle + random.randint(-30,30)  #bounce of the screen
    ball.angle %= 360
    #makes sure the ball goes up after hitting the paddle
    if (ball.angle < 20):
      ball.angle = 20
    elif (ball.angle > 160):
      ball.angle = 160
    score += 1
    if (score == 5):
      paddle.width -= 5

  ball.angle %= 360  #ensures angle is vaild
  score_test = "Score:" + str(score)


play.start_program()
