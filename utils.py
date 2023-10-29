import numpy as np
import cv2

# function for creating canvas
def create_cluster_canvas(shape=(1000,1000),n_clusters=4,mean_x=50, mean_y=30, stdv=10):
    canvas = np.zeros(shape)
    yc, xc = shape[0]//2, shape[1]//2
    on_angle = 360/n_clusters

    if on_angle==90:
        points_mean = [(np.random.randint(xc,shape[1]),yc), (xc,np.random.randint(0,yc)),
                       (np.random.randint(0,xc),yc),(xc,np.random.randint(yc, shape[0]))]
    else:
        print("Else")

    ppoints=[]
    for cpts in points_mean:
        x,y = np.random.normal(cpts[0], stdv, n_clusters), np.random.normal(cpts[1], stdv, n_clusters)
        new_ln = [(int(x[i]),int(y[i])) for i in range(len(x))]

        ppoints.extend(new_ln)

    for i in ppoints:
        canvas = cv2.circle(canvas,i,3,(255,255,255),-1)


    cv2.imshow("canvas",canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return canvas



m =create_cluster_canvas()


