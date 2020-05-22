import random
dx=[0,1,0,-1]
dy=[1,0,-1,0]
    
def learning(x,y):
    global Q,arr
    if arr[x][y] == 'H' or arr[x][y] == 'G':
        return
    
    idx = list(Q[x][y].keys())
    state =  idx[random.randint(0,len(idx)-1)]
    nx = x+dx[int(state)]
    ny = y+dy[int(state)]

    if arr[nx][ny] == 'H':
       Q[x][y][state]=-1
    elif arr[nx][ny] == 'G':
        Q[x][y][state]=1
    else:    
        Q[x][y][state] = 0.5*max(Q[nx][ny].values())
        
    learning(nx,ny)
    
def FrozenLake(m,n,inp):
    global Q,arr
    arr = [[0 for x in range(n)] for y in range(m)]
    Q = [[0 for x in range(n)] for y in range(m)]
    i=0
    sx=0
    sy=0
    for x in inp:
        j=0
        for y in x:
            if y != '\n':
                arr[i][j] = y
                if arr[i][j] == 'S':
                    sx=i
                    sy=j
                Q[i][j]={}
                for q in range(4):
                    if i+dx[q]<m and i+dx[q]>=0 and j+dy[q]<n and j+dy[q]>=0:
                        Q[i][j][q] = 0
            j+=1
        i+=1

    i=0
    while i<100000:
        i+=1
        learning(sx,sy)
        if 0 in list(Q[sx][sy].values()):
            i-=1

    return (sx,sy)

def play(opt,k,m,n,x,y):
    global Q,arr
    while True:
        val = list(Q[x][y].values())
        key = list(Q[x][y].keys())
        ni = int(key[val.index(max(val))])
        x = x+dx[ni]
        y = y+dy[ni]
        if arr[x][y] == 'G':
            break
        arr[x][y] = 'R'
    
    f = open("FrozenLake_%s_output.txt" %k, "w")
    f.write(opt)
    for i in range(m):
        for j in range(n):
            f.write(arr[i][j])
        f.write('\n')   
    f.close()

#main
for i in range(1,4):
    f = open("FrozenLake_%d.txt" % i, "r")
    opt = f.readline()
    k,m,n = opt.split()
    inp  = f.readlines()
    f.close()
    
    s = FrozenLake(int(m),int(n),inp)
    play(opt,k,int(m),int(n),s[0],s[1])
