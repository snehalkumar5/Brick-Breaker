## BRICK BREAKER
### DASS ASSIGNMENT - 2

### The game- A version of brick breaker arcade game made using Python3. Player uses paddle to guide the ball and smash the bricks and get the highest score.
### How to play
python3 main.py
e - To start game
a - To move paddle left
d - To move paddle right
space - To use grab
q - To quit

### Features
### OOPS:
Inheritance: Classes inherit attributes and methods of parent class.
Polymorphism: Used function overloading for polymorphism. Function behaves differently based on the parameters passed when called.
Encapsulation: The methods used in calls are through objects of classes. This encapsulates the attributes of the object.
Abstraction: Functions like check_collision(), move_ball() are made intuitive by hiding the inner details of the function from the user.

### Collisions: 
1. Ball and paddle 
2. Ball and wall
3. Ball and bricks

### Bricks
BasicBrick - has 1 hp (breaks on one hit)
PremiumBrick - has 2hp
UltraBrick - has 3hp
SolidBrick - unbreakable brick (breaks only due to exploding brick or Thru-ball powerup)
ExplodeBrick - explodes and breaks neighboring bricks as well

### Powerups 
Spawns randomly from broken bricks, Activated on contact with paddle.
Lasts for 10 secs each
1. Expand paddle
2. Shrink Paddle
3. Ball Multiplier
4. Fast Ball
5. Thru-ball
6. Paddle Grab

