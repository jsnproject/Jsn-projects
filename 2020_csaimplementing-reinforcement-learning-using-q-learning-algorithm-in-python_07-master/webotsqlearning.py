#time.sleep() subject to change


import random
import time

from controller import Robot, DistanceSensor, Motor

TIME_STEP = 64
MAX_SPEED = 6.28

robot = Robot()

ps = []
psNames = ['ps0','ps1','ps2','ps3','ps4','ps5','ps6','ps7']



for i in range(8):
    ps.append(robot.getDistanceSensor(psNames[i]))
    ps[i].enable(TIME_STEP)
    
leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')    
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)








ALPHA=0.1 #LEARNING RATE
GAMMA=0.5 #DISCOUNT RATE
EPSILON= 0.90#EXPLORATION FACTOR
EPISODES=100
ACTION=0#(0:FORWARD,1:BACKWARD,2:stop,3:LEFT)
ACTION_TAKEN=False
STATES=10
ACTIONS=[1,2,3,4]
NO_OF_ACTIONS=4
Q=[]
Q.append([0.0,0.0,0.0,0.0])
Q.append([0.0,0.0,0.0,0.0])
Q.append([0.0,0.0,0.0,0.0])
Q.append([0.0,0.0,0.0,0.0])
Q.append([0.0,0.0,0.0,0.0])
Q.append([0.0,0.0,0.0,0.0])
Q.append([0.0,0.0,0.0,0.0])
Q.append([0.0,0.0,0.0,0.0])
Q.append([0.0,0.0,0.0,0.0])
Q.append([0.0,0.0,0.0,0.0])
    
REWARDS= []
REWARDS.append([-10,-2,-1,10])
REWARDS.append([-10,-2,-1,10])
REWARDS.append([-10,-2,-1,10])
REWARDS.append([-10,-2,-1,10])
REWARDS.append([-10,-2,-1,10])
REWARDS.append([-10,-2,-1,10])
REWARDS.append([-10,-2,-1,10])
REWARDS.append([-10,-2,-1,10])
REWARDS.append([-10,-2,-1,10])
REWARDS.append([-10,-2,-1,10])

def forward():
        leftSpeed = 0.5*MAX_SPEED
        rightSpeed = 0.5*MAX_SPEED
        leftMotor.setVelocity(leftSpeed)
        rightMotor.setVelocity(rightSpeed)
        
def backward():
        leftSpeed = -0.5 * MAX_SPEED
        rightSpeed = -0.5 * MAX_SPEED
        leftMotor.setVelocity(leftSpeed)
        rightMotor.setVelocity(rightSpeed)
        
def left():
        leftSpeed -= 0.5 * MAX_SPEED
        rightSpeed += 0.5 * MAX_SPEED
        leftMotor.setVelocity(leftSpeed)
        rightMotor.setVelocity(rightSpeed)


def right():
        leftSpeed += 0.5 * MAX_SPEED
        rightSpeed -= 0.5 * MAX_SPEED
        leftMotor.setVelocity(leftSpeed)
        rightMotor.setVelocity(rightSpeed)

def stop():
        leftSpeed = 0
        rightSpeed = 0
        leftMotor.setVelocity(leftSpeed)
        rightMotor.setVelocity(rightSpeed)

def Obstacle_Avoider(): # should return True or False
        psValues = []
        for i in range(8):
                psValues.append(ps[i].getValue())
        obstacle = psValues[0] >80.0 and psValues[7] > 80.0
        return obstacle




def RANDOM(EXPLORATION_PARAMETER):
	RANDOM_VAR=random.randint(0, 100)
	PROB=(RANDOM_VAR/100)
	return PROB
def DECAY(PARAMETER):
	PARAMETER=float(PARAMETER)*0.98
	return PARAMETER
def GET_STATE():
	STATE_NO=random.randint(0, 10)
	return STATE_NO

Q_TABLE=[]

def MAX(Q_TABLE,NEXT_S):   #may cause an error
	LIST=[]
	MAX_VALUE=0.0
	b=0
	while b<=3:
		LIST.append(Q[NEXT_S][b]) #may cause an error
		b=b+1
	j=0
	while j<=2:
		if MAX_VALUE>LIST[j]:
			N1=MAX_VALUE
		else:
			N1=LIST[j]
		N2=LIST[J+1]
		DIFF= N1-N2
		if DIFF>0:
			MAX_VALUE=N1
		else:
			MAX_VALUE=N2
		j=j+1
	return MAX_VALUE
def ARGMAX(Q_TABLE,S):     #may cause an error
	ARRAY=[]
	MAX_VALUE=0.0
	u=0
	while u<=3:
		ARRAY.append(Q[S][u])   #may cause an error
		u=u+1
	p=0
	while p<=2:
		if MAX_VALUE>ARRAY[j]:
			N1=MAX_VALUE
		else:
			N1=ARRAY[j]
		N2=LIST[p+1]
		DIFF= N1-N2
		if DIFF>0:
			MAX_VALUE=N1
		else:
			MAX_VALUE=N2
		p=p+1
	r=0
	while r<=3:
		NUM=ARRAY[r]
		if NUM==MAX_VALUE:
			MAX_INDEX=r
			break
		r=r+1
	return MAX_INDEX

def UPDATE(Q_TABLE,S,NEXT_S,A,ACTIONS,R,LEARNING_RATE,DISCOUNT_FACTOR):
    Q_OLD=Q_TABLE[S][A]
    Q_MAX = MAX(Q_TABLE, NEXT_S)
    Q_NEW = (1-LEARNING_RATE)*Q_OLD + LEARNING_RATE*(R + DISCOUNT_FACTOR*Q_MAX)
    print('Q value:' + Q_NEW)
    Q_TABLE[S][A] = Q_NEW




def loop():
    I=0
    while I<EPISODES:
        print('START:')
        ACTION_TAKEN= False
        FLAG=0
        while True:
            forward()
            Obstacle=Obstacle_Avoider()
            if Obstacle== True:
               NEXT_STATE=STATE+1
            if NEXT_STATE==10:
                NEXT_STATE=0
        	 if NEXT_STATE<0:
                NEXT_STATE=0
            print('STATE:')
        	 print('       ' + STATE)
        	 FLAG=1
        	 break
        	   
            if FLAG==1:
                PROB= RANDOM(EPSILON)
        	 if PROB<=EPSILON:
                ACTION=random.randint(0, 4)
                FLAG=2
        	 else:
                ACTION=ARGMAX(Q,STATE)
                FLAG=2
        		
            if FLAG==2:
                if ACTION==0:
                    forward()
                    time.sleep(1.5) #subject to change
                    stop()
                    REWARD= REWARDS[STATE][ACTION]
                if ACTION==1:
                    backward()
                    time.sleep(2.5)
                    stop()
                    REWARD= REWARDS[STATE][ACTION]	
                if ACTION==2:
                    stop()
                    REWARD= REWARDS[STATE][ACTION]	
                if ACTION==3:
                    left()
                    time.sleep(2)
                    stop()
                    REWARD= REWARDS[STATE][ACTION]
                    ACTION_TAKEN=True
                    time.sleep(0.5)
    		
    		
                if ACTION_TAKEN == True:
                    UPDATE(Q,STATE,NEXT_STATE,ACTION ,ACTIONS,REWARD,ALPHA ,GAMMA)
                    STATE = NEXT_STATE
                    EPSILON = DECAY(EPSILON)
                    if EPSILON<0.5:
                        EPSILON  == 0.9
                    print('EPISODE ENDED:')
                    print('     ' + I)
                    time.sleep(7)
                    I=I+1
                
    y=0
            
    while y<=9: 
      print('SET OF Q VALUES WILL START:')
      l=0
      while l<=3
          print('Q VALUE :')
          print(Q[y][l] +'\n')
          time.sleep(2)
          l=l+1
      time.sleep(2)
      y=y+1
      print('EVALUATION ENDED')
    while True:
        forward()
        Obstacle = Obstacle_Avoider() #webots this is where the sensor is there or not if true or false
        if Obstacle == true:
            STATE = GET_STATE()
            ACTION = ARGMAX(Q,STATE)
            print('ACTION TAKEN: ')
            print(ACTION + '\n')
            if ACTION ==0:
                forward()
                time.sleep(1.5)
                stop()
            if ACTION == 1:
                backward()
                time.sleep(1.5)
                stop()
            if ACTION == 2:
                stop()
            if ACTION == 3:
                left()
                time.sleep(2)
                stop()
       

