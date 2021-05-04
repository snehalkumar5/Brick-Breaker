## BRICK BREAKER

### The game- A version of brick breaker arcade game made using Python3. Player uses paddle to guide the ball and smash the bricks and get the highest score.
### How to play
`python3 main.py `

e - To start game\
a - To move paddle left\
d - To move paddle right\
space - To use grab\
q - To quit\
t - To skip to next level

### Features
### Paddle and Player:
Player uses paddle to redirect the ball to break as many bricks possible.
### Bricks:
There are a total of 5 kinds of bricks:
Basic Brick - 1hp\
Premium Brick - 2hp\
Ultra Brick - 3hp\
Exploding Brick - Explodes itself and its neighbouring bricks on collision with ball\
Unbreakable Brick - cannot be broken

#### Multiple Levels:
3 levels with different layouts. Use key 'T' to skip through.\
Changing levels:\
Loses all powers\
Score carries over

#### Falling bricks
After a set time (FALLING_TIME, default=70), the bricks drop by one unit towards the paddle when the ball hits the paddle. On reaching the bottom, game ends.

#### Boss Enemy:
Last level has a Final Boss - UFO\
Drops bomb every interval (BOMB_SHOOT,default=3sec).\
Loses 1hp on collision with ball\
Loses 2hp on collision with bullet\
Gains 1000 points on beating the boss\
Spawns a defense array below it twice on reaching certain health (6hp,2hp)\
Defense array doesn't drop powerups

#### Rainbow Bricks:
Changes colours every frame. On collision appears as a normal brick with same features as that of when collision occurred.

#### Powerups:
All powerups now drop with a velocity corresponding to the ball. Drops have gravity factor.
1. Shooting Paddle: Continuously shoots bullets from paddle with an interval (SHOOT_PADDLE, default=1sec) between successive bullets. Shows time left in navbar.\
Paddle grows cannons to shoot bullets
2. Fireball: On collision with brick and ball, bricks explode along with its neighbours


