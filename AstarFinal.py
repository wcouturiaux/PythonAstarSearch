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

def createPath(cameFrom,curNode):
    path = [curNode]
    while curNode in cameFrom.keys():
        curNode = cameFrom[curNode]
        path.append(curNode)
    path = path[::-1]
    return path

def shortest_path(M,start,goal):
    #initialize sets for frontier and explored
    frontier = {start:0}#Visited not expanded
    explored = set()#visited and expanded
    gScore={}
    gScore[start]=0
    path=[]
    curGScore=0
    cameFrom={}
    
    #initialize current state
    curNode = start
    
    while frontier: #execute code while frontier is not empty
        curNode = min(frontier, key=frontier.get)

        if curNode==goal:
            return createPath(cameFrom,curNode)

        frontier.pop(curNode)
        explored.add(curNode)

        curInts = M.roads[curNode]

        for item in curInts:
            if item in explored:
                continue

            if item not in frontier:
                frontier[item] = gScore[curNode] + fscore(M,item,curNode,goal)

            newgscore = gScore[curNode] + gscore(M,curNode,item)
            if item in gScore and newgscore>=gScore[item]:
                continue

            cameFrom[item] = curNode
            gScore[item]=newgscore
            frontier[item] = gScore[item]+hscore(M,item,goal)
                    
    
    print("shortest path called")
    return
    