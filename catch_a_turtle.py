# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
leaderboard_file_name= "a122_leaderboard.txt"
leader_names_list=[]
leader_scores_list=[]
player_name= input("what's your name")
spot_color = "pink"
spot_shape="circle"
spot_size=2 


#-----initialize turtle-----
spot=trtl.Turtle()
spot.shape(spot_shape)
spot.turtlesize(spot_size)
spot.fillcolor(spot_color)
score_writer= trtl.Turtle()
score_writer.penup()
score_writer.goto(-200,200)
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter =  trtl.Turtle()
counter.penup()
counter.goto(200,200)
colors=["purple","yellow","blue","red","white","brown"]
sizes=[0.5,1,1.5,2,2.5,3,3,5,4]

#-----game functions--------
font_setup=("Arial", 20, "normal")
score=0
def update_score():
  global score 
  score += 1
  score_writer.clear()
  score_writer.write("score:" + str(score), font=font_setup)

def change_position():
  new_xpos=rand.randint(-200,200)
  new_ypos= rand.randint(-150,150)
  spot.goto(new_xpos,new_ypos)

def spot_clicked(x,y):
  if timer_up== False:
     spot.penup()
     spot.hideturtle()
     change_position()
     spot.showturtle()
     update_score()
     adding_color()
     change_size()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 



def adding_color():
  spot.fillcolor(rand.choice(colors))
  spot.stamp()
  spot.fillcolor("pink")

def change_size():
  spot.turtlesize(rand.choice(sizes))

def start_game():
  if True:
    spot.onclick(spot_clicked)
    countdown()

start_game()

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)
#-----events----------------

wn = trtl.Screen()
wn.bgcolor("teal")
wn.mainloop()
