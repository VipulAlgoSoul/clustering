from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
import numpy as np
import cv2
import random
import math
from ast import literal_eval

X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0,center_box=(1.0, 20.0))


# print(X,y_true)

plt.scatter(X[:, 0], X[:, 1], s=50);
plt.show()

#set cluster
#select 4 cluster number
#select random 4 points



def point_belong(key_points , point):
    min_pnt = 10000
    ptr = None
    for kp in key_points:
        nd = math.dist(kp,point)
        # print(kp, point, nd)
        if nd<min_pnt:
            min_pnt=nd
            ptr=kp
    # print(ptr,">>>>")
    return ptr

centers = np.array(random.sample(list(X),4))
prv_centers = None
while(True):
    plt.figure()
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
    # plt.show()

    cnt_dc = {i:p for i,p in enumerate(centers)}
    centre_dict = {str(i):[] for i in cnt_dc.values()}
    prv_centre_dict = centre_dict.copy()
    prv_centers = centers
    centers=[]
    for pnts in X:
        centre_dict[str(point_belong(cnt_dc.values(),pnts))].append(pnts)
    clr_dict ={0:"black",1:"blue",2:"red",3:"yellow"}
    cnt=0

    for k,va in centre_dict.items():
        if va:
            v=np.array(va)
            plt.scatter(v[:, 0], v[:, 1], c=clr_dict[cnt], s=200, alpha=0.5);
            cnt+=1
            #find avrg of x and ys
            #remove the str and replace with new
            xavg = np.mean(np.array([i[0] for i in va]))
            yavg = np.mean(np.array([i[1] for i in va]))
            centers.append([xavg,yavg])

        else:
            centers.appendliteral_eval(k)

    centers = np.array(centers)
    if np.array_equal(centers, prv_centers):
        print("Found Final Cluster")
        # plt.title("Final Clusters")
        plt.show()
        break

    # plt.show()
    #calculate new centres

