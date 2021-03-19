## BRICK BREAKER
### DASS ASSIGNMENT - 2
### Snehal Kumar

### The game- A version of brick breaker arcade game made using Python3. Player uses paddle to guide the ball and smash the bricks and get the highest score.
### How to play
python3 main.py
e - To start game
a - To move paddle left
d - To move paddle right
space - To use grab
q - To quit
t - To skip to next level

### Features
#### Multiple Levels:
3 levels with different layouts. Use key 'T' to skip through.
Changing levels:
Loses all powers
Score carries over

#### Falling bricks
After a set time (FALLING_TIME, default=70), the bricks drop by one unit towards the paddle when the ball hits the paddle. On reaching the bottom, game ends.
```python
if (todrop == 1 and time_passed>=FALLING_TIME):
	step=1
	todrop=0
flag = bricksshow(myboard.grid,bricks_arr,mypaddle,step)
```
#### Boss Enemy:
Last level has a Final Boss - UFO
Drops bomb every interval (BOMB_SHOOT,default=3sec).
Loses 1hp on collision with ball
Loses 2hp on collision with bullet
1000 points on beating the boss
Spawns a defense array below it twice on reaching certain health (6hp,2hp)
Defense array doesn't drop powerups

#### Rainbow Bricks:
Changes colours every frame. On collision appears as a normal brick with same features as that of when collision occurred.

#### Powerups:
All powerups now drop with a velocity corresponding to the ball. Drops have gravity factor.
1. Shooting Paddle: Continuously shoots bullets from paddle with an interval (SHOOT_PADDLE, default=1sec) between successive bullets. Shows time left in navbar.
Paddle grows cannons to shoot bullets
2. Fireball: On collision with brick and ball, bricks explode along with its neighbours (#BONUS)

#### Game sounds: 
Added game sounds for (#BONUS)
1. Ball collisions
2. Explosion
3. Powerup gained
4. Life lost
5. Game start
6. Boss enters
7. Boss hit
8. Game Over
9. Game Win
10. Shoot bullets

