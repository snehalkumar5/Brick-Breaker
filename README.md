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

### Features
### OOPS:
Inheritance: Classes inherit attributes and methods of parent class.
```python
class  Brick:
	"""Parent"""
	def  __init__(self, x, y,pow):
		self._x = x
		self._y = y
		
class  BasicBrick(Brick):
	"""Child inherits"""
	def  __init__(self, x, y, power):
		Brick.__init__(self, x, y, power)
```
Polymorphism: Used function overloading for polymorphism. Function behaves differently based on the parameters passed when called.
```python
class  Player():
	"""
	Player class
	"""
	def  show(self,grid,figure,x,y):
		for i in  range(len(figure)):
		for j in  range(len(figure[i])):
		grid[y+i][x+j]=figure[i][j]
		
class  Ball(Player):
	"""
	Class for Ball
	"""
	def  __init__(self,x,y):
		self.fig = np.array([BALL])
		Player.__init__(self,x,y)
		
	def  show(self,grid,x,y):
		self.clear_ball(grid)
		self.set_coord(x,y)
		grid[y][x]=self.fig[0]
```
Encapsulation: The methods used in calls are through objects of classes. This encapsulates the attributes of the object.
```python
mynav = Navbar(FRAME_WIDTH)
mynav.print_header(timeleft,mypaddle,bricks_arr)
```
Abstraction: Functions like check_collision(), move_ball() are made intuitive by hiding the inner details of the function from the user.

### Collisions: 
1. Ball and paddle 
2. Ball and wall
3. Ball and bricks

### Bricks
Change colour when health decreases
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

