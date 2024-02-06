import random
from turtle import Turtle
COLORS=["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10

#CARS WILL MOVE RIGHT TO LEFT & WILL BE RANDOMLY GENERATED ALONG WITH Y AXIS
class CarManager:
    
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    
    #IT WILL CREATE A RANDOM CAR SOMEWHERE ALONG THE Y AXIS WITH GIVEN DIMENSION
    def create_car(self):
        #TOO MANY CARS ARE GENERATED EACH TIME A CREATE_CAR FUNCTION IS CALLED
        #SO TO REDUCE NUMBER OF GENERATED CAR WE WILL GENERATE CAR ONLY IF RANDOM_CHANCE=1
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
     
    #IT WILL MOVE THE CARS     
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    #IT WILL LEVEL UP THE SPEED WHEN THE LEVELS OF GAME WILL INCREASE        
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT       