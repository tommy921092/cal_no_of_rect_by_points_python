import math
import time
from itertools import product, combinations
filepath = 'f3.txt'
result=0
startTime = time.time()
with open(filepath) as fp:
   points = fp.readline()
   cnt = 1
   my_list=list()
   while points:
    #    print("points {}: {}".format(cnt, points.strip()))
       points.strip()
       my_list.append(tuple([float(points.split(',')[0]), float(points.split(',')[1].split('\n')[0])]))
       points = fp.readline()
       my_list = list(dict.fromkeys(my_list))
       print("my_list:", my_list)
       cnt += 1

list_of_four = list(combinations(my_list, 4))

def calDistanceSq(pt1, pt2):
    [x1,y1] = pt1
    [x2,y2] = pt2
    distsq = (x2 - x1)**2 + (y2 - y1)**2
    return distsq

def collinear(points):
    ([x1,y1],[x2,y2],[x3,y3])=points
    return ((y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2))

def formRect(points):
    counter=0
    list_of_three = list(combinations(points,3))
    for pts in list_of_three:
        if collinear(pts):
            return False
    ([x1,y1], [x2,y2], [x3,y3], [x4,y4]) = points
    dist12sq = calDistanceSq([x1,y1], [x2,y2])
    dist13sq = calDistanceSq([x1,y1], [x3,y3])
    dist14sq = calDistanceSq([x1,y1], [x4,y4])
    dist23sq = calDistanceSq([x2,y2], [x3,y3])
    dist24sq = calDistanceSq([x2,y2], [x4,y4])
    dist34sq = calDistanceSq([x3,y3], [x4,y4])
    listDist = [dist12sq,dist13sq,dist14sq,dist23sq,dist24sq,dist34sq]
    listDist.sort()
    if listDist[4]!=listDist[5]:
        return False
    if listDist[0]+listDist[1]==listDist[4]:
        counter+=1
    if listDist[0]+listDist[2]==listDist[4]:
        counter+=1
    if listDist[0]+listDist[3]==listDist[4]:
        counter+=1
    if listDist[1]+listDist[2]==listDist[4]:
        counter+=1
    if listDist[1]+listDist[3]==listDist[4]:
        counter+=1
    if listDist[2]+listDist[3]==listDist[4]:
        counter+=1
    if counter>=2:
        return True
for points in list_of_four:
    if (formRect(points)):
        print(str(points))
        result +=1

print(f'{result} rectangles found for give points of {cnt-1}')
print(f'Time Taken: {time.time()-startTime}')