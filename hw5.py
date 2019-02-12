import math
"""
Daniel Mevs
HW 5
"""

def f(x,y):
    return(((x-1)**2)-(4*(x-1)*(y-3))+(5*((y-3)**2)) - 841)

def main():
    acc = []
    roots = []
    
    min_x = -61
    max_x = -21
    min_y = -26
    max_y = 3
    
    farthest_pnt = (-21, 0)
    farthest_dist = sum([i**2 for i in farthest_pnt])**(1/2)
    closest_pnt = (-61, -27)
    closest_dist = sum([i**2 for i in closest_pnt])**(1/2)
    farthest_r_dist = 0
    closest_r_dist = 5000


    for i in range(-1600,800):
        for j in range(-1600,800):
            z=f(i,j)
            if(z<=0):
                acc+=[(i,j)]
                if(i<min_x):
                    min_x = i
                if(i>max_x):
                    max_x = i
                if(j<min_y):
                    min_y = j
                if(j>max_y):
                    max_y = j
                d=math.sqrt((i*i)+(j*j))
                if(d < closest_dist):
                    closest_dist = d
                    closest_pnt = (i,j)
                if(d > farthest_dist):
                    farthest_dist = d
                    farthest_pnt = (i,j)
                if z==0:
                    roots+=[(i,j)]
                    if(d < closest_r_dist):
                        closest_r_dist = d
                        closest_r_pnt = (i,j)
                    if(d > farthest_r_dist):
                        farthest_r_dist = d
                        farthest_r_pnt = (i,j)
                
    #print("The latice points are"+str(acc))
    print("The number of latice points in C are ", len(acc))
    #roots = sum([f(i[0],i[1]) for i in acc] == 0)
    print("The number of latice points on the boundary is ", len(roots))
    print("The minimum x value for all lattice points in C is ", min_x)
    print("The maximum x value for all lattice points in C is ", max_x)
    print("The minimum y value for all lattice points in C is ", min_y)
    print("The maximum y value for all lattice points in C is ", max_y)
    print("The lattice point closest to  the origin in C is ", closest_pnt)
    print("The lattice point farthest from  the origin in C is ", farthest_pnt)
    print("The lattice point farthest from the origin on the boundary of C is ", farthest_r_pnt)
    print("The lattice point closest from the origin on the boundary of C is ", closest_r_pnt)
    
if __name__ == '__main__':
    main()
