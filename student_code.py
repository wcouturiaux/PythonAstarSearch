import math
import pdb

def dist(x1,y1,x2,y2):
    dist = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    
    return dist

def gscore(M,node1,node2):
    g = dist(M.intersections[node2][0], M.intersections[node2][1],
             M.intersections[node1][0], M.intersections[node1][1])
    return g

def hscore(M,node1,goal):
    h = dist(M.intersections[node1][0], M.intersections[node1][1],
             M.intersections[goal][0], M.intersections[goal][1])
    return h

def fscore(M, key, curNode, goal):
    f = gscore(M,key,curNode) + hscore(M, key,goal)
    return f

def shortest_path(M,start,goal):
    #initialize sets for frontier and explored
    frontier = {start:0}#Visited not expanded
    explored = set()#visited and expanded
    path=[]
    curGScore=0
    #initialize costs
    #g = 0 #actual path cost
    #h = 0 #estimated cost from current state to goal
    #f = 0
    
    #initialize current state
    curNode = start
    
    while frontier: #execute code while frontier is not empty
        #pdb.set_trace()
        prevNode = curNode            
        curNode = min(frontier,key=frontier.get) #assign low f node to be current
        curGscore = gscore(M,prevNode,curNode)
        if curNode == goal:
            path.append(curNode) #add to path
            break
        path.append(curNode) #add to path
        explored.add(curNode) #add current node to explored
        frontier.pop(curNode) #remove current node from frontier
        curIntersects = M.roads[curNode] #find paths connected to current node
       # pdb.set_trace()
        for item in curIntersects:    
            if item in explored: #if connected node already explored next node
                continue
            #pdb.set_trace()
            if item not in frontier:
                frontier[item]=fscore(M,item, curNode, goal)+curGscore
        for item in curIntersects:
            if item in explored:
                continue
               
            newfscore = 0
            newfscore = curGscore + fscore(M,item,curNode, goal)
            #pdb.set_trace()
            if newfscore < frontier[item]:
                frontier[item]=newfscore

            elif newfscore>frontier[item]:
                curGscore -=gscore(M,prevNode,curNode)
                #frontier.pop(curNode)
                path.remove(curNode)
                curNode=prevNode
                break
                #explored.add(curNode)
            else:
                continue
                
                
        #if goal in explored:
         #   break
                    
    
    print("shortest path called")
    return path
    