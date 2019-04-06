import math
import pdb
from queue import PriorityQueue

def dist(x1,y1,x2,y2):
    """Calculate the euclidean distance between two points"""
    dist = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    
    return dist

def gscore(M,node1,node2):
    """calculate the euclidean distance between two points on a given map"""
    g = dist(M.intersections[node2][0], M.intersections[node2][1],
             M.intersections[node1][0], M.intersections[node1][1])
    return g

def hscore(M,node1,goal):
    """Calculate the Euclidean distance between a point and the goal point for a given map"""
    h = dist(M.intersections[node1][0], M.intersections[node1][1],
             M.intersections[goal][0], M.intersections[goal][1])
    return h

def fscore(M, key, curNode, goal):
    """Calculate the priority score or score between two nodes plus the score of the end node to the goal"""
    f = gscore(M,key,curNode) + hscore(M, key,goal)
    return f

def createPath(cameFrom,curNode):
    """Recreate the path traveled in the shortest distance function"""
    path = [curNode] #Initialize Path
    while curNode in cameFrom: #while the current node is in the dictionary cameFrom
        curNode = cameFrom[curNode] #change curNode to its parent node
        path.append(curNode) #append the parent node to path
    path = path[::-1] #reverse the order of the path as it was created starting at the goal
    return path

def shortest_path(M,start,goal):
    """Find the shortest path between two nodes on a given map"""
    #Check if the start and goal nodes are integers if not assert error that they are not of valid type
    if not isinstance(start,int) or not isinstance(goal,int):
        raise AssertionError("Start or Goal not a vaild input")
    
    frontier = PriorityQueue()#initialize a priority queue for the frontier
    
    frontier.put((0,start)) #place the start node in the frontier (score,node)
    
    explored = set() #track visited and expanded nodes 
    
    gScore={} #dictionary to keep track of a nodes gscore
    
    gScore[start]=0 #set start nodes gscore to zero
    
    cameFrom={} #initialize a dictionary to track the path traveled
    
    
    while True: 
        curNode = frontier.get()[1] #set current node to the lowest fscore node in the frontier.
        
        #if the current node is the goal call create path and return
        if curNode==goal:
            
            return createPath(cameFrom,curNode)

        
        explored.add(curNode) #add the current node to the explored set

        curInts = M.roads[curNode] #assign nodes connected to the current node to curInts
        
        #For each connected node loop
        for item in curInts:
            
            # if item(current connected node) has already been explored move to next connected node
            if item in explored:
                continue
            
            #calculate the g score of the current node
            newgscore = gScore[curNode] + gscore(M,curNode,item)
            
            #if the gscore to the current item is higher than from previous node skip to next item
            if item in gScore and newgscore>=gScore[item]:
                
                continue

            cameFrom[item] = curNode #assign current node to came from (path)
            
            gScore[item]=newgscore #update items gscore
            
            frontier.put(((gScore[item]+hscore(M,item,goal)),item)) #update or add item to frontier
                    
    
    print("shortest path called")
    return print("No Path found between start and goal")
    