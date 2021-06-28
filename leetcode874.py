class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        for i in range(len(obstacles)):
            obstacles[i]=tuple(obstacles[i])
        obstacles=set(obstacles)    
        dx=[0,1,0,-1]   
        dy=[1,0,-1,0]
        direction=0
        x=0
        y=0
        res=0
        for com in commands:
            if com==-2:
                direction=(direction+3)%4
            elif com==-1:
                direction=(direction+1)%4
            else:
                for k in range(1,com+1):
                    next_x=x+dx[direction]
                    next_y=y+dy[direction]
                    if (next_x,next_y) not in obstacles:
                        x=next_x
                        y=next_y
                    res=max(res,x*x+y*y)
        return res
        
