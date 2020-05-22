#bfs
def bfs(x,y,finish):  #인자로 시작좌표(x,y)와 도착지점의 값(finish)을 받음 
    global arr,bfs_ans,xn,yn   #적역변수로 사용 arr:입력받은 값, xn,yn:4방향 탐색을 위한 배열, bfs_ans답을 저장하는 배열 
    bfs_step = [[0 for x in range(int(m))] for y in range(int(n))]   #역추적을 위한 2차원배열 선언 
    
    queue = []   #큐 선언 
    queue.append((x,y))   #큐에 시작좌표 추가
    for i in range(int(m)):    
        for j in range(int(n)):
            bfs_step[i][j] = -1   #역추적 배열-1로 초기화
            
    time=0   #탐색하는 노드 수를 세는 변수 
    bfs_step[x][y] = 4   #시작점의 역추적값은 4로 설정 
    while len(queue) > 0:   #큐에 값이 존재하면 반복 
        x = queue[0][0]   #까장 먼저 들어온 x,y좌표를 받아옴 
        y = queue[0][1]
        if arr[x][y] == finish:   #도착지점에 도달하면 탐색 종료 
            break
        del queue[0]   #큐에서 가장 먼저 들어온 값을 빼줌 
        time+=1   #탐색한 노드 갯수 증가 
        for i in range(4):   #4방향 모두 탐색해줌
            nx = x+xn[i]   #연결된 좌표값 
            ny = y+yn[i]
            if nx < 0 or ny < 0 or nx >= int(m) or ny >= int(n):   #범위를 넘어서면 무시 
                continue
            if (arr[nx][ny] == 2 or arr[nx][ny] == finish) and bfs_step[nx][ny] == -1:   #이동 가능한 좌표이고 방문하지 않은 좌표이면 탐색 
                queue.append((nx,ny))   #큐에추가 
                bfs_step[nx][ny] = i   #역추적을 위해 표기
                
    #역추적은 모든 탐색방법에서 동일하게 상용 
    rx = x
    ry = y
    length=0
    while bfs_step[rx][ry]<4:   #시작지점에 도달할 때 까지 반복
        length+=1
        bfs_ans[rx][ry] = 5   #지나간 좌표는 5로 바꿔줌 
        for i in range(4):
            if bfs_step[rx][ry] == i:   #이전에 방문했던 노드로 이동 
                rx-=xn[i]
                ry-=yn[i]
                break
            
    bfs_ans[x][y] = finish   #도착좌표의 값은 원래대로 바꿔줌  
    return (x,y,time,length)  #도착좌표(x,y)와 탐색도느갯수(time), 최소이동거리(length) 반환 
#-----------------------------bfs

#ids
def ids(ix,iy,finish):   #인자로 시작좌표(ix,iy)와 도착지점의 값(finish)을 받음 
    global arr,ids_ans,xn,yn   #적역변수로 사용 arr:입력받은 값, xn,yn:4방향 탐색을 위한 배열, ids_ans답을 저장하는 배열 
    ids_step = [[0 for x in range(int(m))] for y in range(int(n))]

    time=0   #방문 노드 갯수 
    limit=0   #탐색깊이 한계 
    while True:   #limit을 증가시키며 답을 찾을 때 까지 반복 
        check=0   #답을 찾았는지 확인하는 변수 
        stack = []   #스택 선언,초기화 
        stack.append((ix,iy,0))   #시작좌표와 깊이를 스택에 넣음 
        for i in range(int(m)):
            for j in range(int(n)):
                ids_step[i][j] = -1   #역추적 배열 -1로 초기화 

        ids_step[ix][iy] = 4
        while len(stack) > 0:   #답을 찾가나 limit을 초과할 때 까지 반복 
            last = len(stack)-1   #스택의 마지막 index를 가르킴 
            x = stack[last][0]   #가장 마지막에 들어온 x,y좌표, 깊이를 가져옴
            y = stack[last][1]
            deep = stack[last][2]
            if arr[x][y] == finish:   #답을 찾으면 종료 
                check=1
                break   
            del stack[last]   #스택에서 빼줌 
            if deep==limit:   #탐색 깊이가 limit보다 커지면 탐색하지 않음 
                continue         
            time+=1   #탐색노드 갯수 증가 
            for i in range(4):   #4방향 모두 탐색 
                nx = x+xn[i]   #다음 x,y좌표 
                ny = y+yn[i]
                if nx < 0 or ny < 0 or nx >= int(m) or ny >= int(n):   #범위를 넘어서면 무시 
                    continue
                if (arr[nx][ny] == 2 or arr[nx][ny] == finish) and ids_step[nx][ny] == -1:   #이동가능한 좌표면 스택에 추가 
                    stack.append((nx,ny,deep+1))   #깊이는 1증가 
                    ids_step[nx][ny] = i   #역추적을 위한 방향 체크 

        if check==1:   #도착점에 도당하면 종료 
            break
        limit+=1   #한계깊이 1증가 
                
    rx = x
    ry = y
    while ids_step[rx][ry]<4:
        ids_ans[rx][ry] = 5     
        for i in range(4):
            if ids_step[rx][ry] == i:
                rx-=xn[i]
                ry-=yn[i]
                break
                
    ids_ans[x][y] = finish
    return (x,y,time,deep)
#-----------------------------ids

#heap
class Heap:   #힙 클래스 선언 
    def __init__(self):   #클래스 선언시 list하나와, 크기를 저장하는 변수 선언 
        self.h = []
        self.size = 0
 
    def build(self,node):   #list와 노드를 받아와서 힙구조를 만들어줌 
        m = node
        if 2*node+1 < self.size and self.h[2*node+1][0] < self.h[m][0]:   #왼쪽 자식노드가 존재하고, 그 값이 현재노드 값보다 작으면 바꿔줌 
            m = 2*node+1
        if 2*node+2 < self.size and self.h[2*node+2][0] < self.h[m][0]:   #오른쪽 자식노드가 존재하고, 그 값이 현재노드 값보다 작으면 바꿔줌
            m = 2*node+2
        if m!=node:   #바꿔야 하는 값이 존재하면 바꾸고, 그 노드부터 다시 빌드
            self.h[node], self.h[m] = self.h[m], self.h[node]
            self.build(m)
 
    def insert(self,hu,x,y,deep):   #list와 노드가 포함해야 하는 정보르 받아서 노드 추가 
        self.h.append((hu,x,y,deep))   #노드 추가 
        cur = self.size   #현재 list크기를 받아옴 
        self.size+=1   #list크기 증가 
        while (cur-1)//2 >= 0 and self.h[cur][0] < self.h[(cur-1)//2][0]:   #자기 위치를 찾아줌, 부모 노드 값이 자기보다 크면 바꿔줌  
            self.h[(cur-1)//2], self.h[cur] = self.h[cur], self.h[(cur-1)//2]   #노드 값 변경 
            cur = (cur-1)//2   #다음 부모 노드 탐색 

    def delete(self):   #list에서 가장 작은 값을 제거 
        cur = self.size   #현재 list사이즈 
        self.h[0] = self.h[cur-1]   #가장 뒤(큰)의 값을 가장 처음 노드에 저장
        self.size-=1   #사이즈 크기 감소 
        del self.h[cur-1]   #마지막에 존재하는 노드 제거 
        self.build(0)   #0번에 가장 큰 값이 존재하므로 0번부터 빌드 시켜줌 
#-----------------------------heap

def huristic(sx,sy,ex,ey):   #현재좌표에서 도착지점까지의 거리는 반환하는 함수,벽을 무시한 거리 
    return abs(ex-sx)+abs(ey-sy)
def finish_xy(finish):   #도착좌표를 찾아서 반환하는 함수 
    global arr
    for i in range(int(m)):
        for j in range(int(n)):
            if arr[i][j] == finish:
                return (i,j)
#gbfs
def greedy_bfs(x,y,finish):   #인자로 시작좌표(x,y)와 도착지점의 값(finish)을 받음
    global arr,gbfs_ans,xn,yn   #적역변수로 사용 arr:입력받은 값, xn,yn:4방향 탐색을 위한 배열, gbfs_ans답을 저장하는 배열
    gbfs_step = [[0 for x in range(int(m))] for y in range(int(n))]
    
    heap = Heap()   #힙 클래스 선언
    f_xy = finish_xy(finish)   #도착좌표를 찾음 
    h = huristic(x,y,f_xy[0],f_xy[1])   #우선순위를 위한 h함수 값 만들기 
    heap.insert(h,x,y,0)   #큐에 인자로 h(우선순위 판단), x,y(현재좌표), 깊이를 가지는 노드 추가 
    for i in range(int(m)):
        for j in range(int(n)):
            gbfs_step[i][j] = -1   #역추적 배열 -1로 초기화 

    time=0   #방문노드 갯수 
    gbfs_step[x][y] = 4         
    while heap.size>0:   #힙이 빌때 까지 반복
        x = heap.h[0][1]   #우선순위가 가장 높은 힙의 x,y좌표, 깊이를 받아옴 
        y = heap.h[0][2]
        deep = heap.h[0][3]
        if arr[x][y] == finish:   #도착지점에 도달하면 종료 
            break        
        time+=1   #방문노드 갯수 증가 
        heap.delete()   #힙에서 노드 삭제 
        for i in range(4):   #4방향 탐색 
            nx = x+xn[i]   #다음 x,y좌표 
            ny = y+yn[i]
            if nx < 0 or ny < 0 or nx >= int(m) or ny >= int(n):   #범위를 넘어서면 무시 
                continue
            if (arr[nx][ny] == 2 or arr[nx][ny] == finish) and gbfs_step[nx][ny] == -1:   #이동가능한 좌표이면 힙에 추가 
                heap.insert(huristic(nx,ny,f_xy[0],f_xy[1]),nx,ny,deep+1)   #이동할 좌표의 h함수, 좌표, 깊이로 새로운 노드를 만듬 
                gbfs_step[nx][ny] = i
                
    rx = x
    ry = y
    while gbfs_step[rx][ry]<4:
        gbfs_ans[rx][ry] = 5     
        for i in range(4):
            if gbfs_step[rx][ry] == i:
                rx-=xn[i]
                ry-=yn[i]
                break
            
    gbfs_ans[x][y] = finish

    return (x,y,time,deep)
#-----------------------------gbfs

#a_star
def a_star(x,y,finish):   #인자로 시작좌표(x,y)와 도착지점의 값(finish)을 받음 
    global arr,a_star_ans,xn,yn   #적역변수로 사용 arr:입력받은 값, xn,yn:4방향 탐색을 위한 배열, a_star_ans답을 저장하는 배열
    a_star_step = [[0 for x in range(int(m))] for y in range(int(n))]
    
    heap = Heap()   #힙 클래스 선언
    f_xy = finish_xy(finish)   #도착좌표를 찾음 
    h = huristic(x,y,f_xy[0],f_xy[1])   #우선순위를 위한 h함수 값 만들기 
    heap.insert(0+h,x,y,0)   #큐에 인자로 h+깊이(우선순위 판단), x,y(현재좌표), 깊이를 가지는 노드 추가 
    for i in range(int(m)):
        for j in range(int(n)):
            a_star_step[i][j] = -1   #역추적 배열 -1로 초기화

    time=0   #방문노드 갯수  
    a_star_step[x][y] = 4         
    while heap.size>0:   #힙이 빌때 까지 반복 
        x = heap.h[0][1]   #우선순위가 가장 높은 힙의 x,y좌표, 깊이를 받아옴 
        y = heap.h[0][2]
        deep = heap.h[0][3]
        if arr[x][y] == finish:   #도착지점에 도달하면 종료
            break
        time+=1   #방문노드 갯수 증가 
        heap.delete()   #힙에서 노드 삭제 
        for i in range(4):   #4방향 탐색
            nx = x+xn[i]   #다음 x,y좌표
            ny = y+yn[i]
            if nx < 0 or ny < 0 or nx >= int(m) or ny >= int(n):   #범위를 넘어서면 무시 
                continue
            if (arr[nx][ny] == 2 or arr[nx][ny] == finish) and a_star_step[nx][ny] == -1:   #이동가능한 좌표이면 힙에 추가 
                heap.insert(huristic(nx,ny,f_xy[0],f_xy[1])+deep,nx,ny,deep+1)   #이동할 좌표의 h함수+깊이, 좌표, 깊이로 새로운 노드를 만듬
                a_star_step[nx][ny] = i
                
    rx = x
    ry = y
    while a_star_step[rx][ry]<4:
        a_star_ans[rx][ry] = 5     
        for i in range(4):
            if a_star_step[rx][ry] == i:
                rx-=xn[i]
                ry-=yn[i]
                break
            
    a_star_ans[x][y] = finish

    return (x,y,time,deep)
#-----------------------------a_star

#output
def output(k,time,length,strr,ans):   #인자로 미로번호, 방문노드 갯수, 최소길이, 알고리즘이름, 결과물을 받아옴 
    f = open("Maze_%d_"%int(k) +strr+"_output.txt", "w")   #형식에 맞춰 쓰기형식으로 파일을 실행 
    
    for i in range(int(m)):
        for j in range(int(n)):
            f.write(str(ans[i][j]))   #미로출력(방문한 좌표는 5)
        f.write('\n')      
    f.write('---\n' )
    f.write('length=%d\n' % length)   #길이출력
    f.write('time=%d\n' % time)   #방문노드 갯수 출력
    f.close()   #파일종료
#-----------------------------output

#process
def Maze(k,n,m,inp):   #미로번호, 미로크기(n,m), 미로를 받아옴
    global arr,bfs_ans,ids_ans,gbfs_ans,a_star_ans,xn,yn   #미로와, 결과물을 저장할 배열, 4방향탐색을 위한배열(xn,yn) 전역변수 선언 
    xn = [1,-1,0,0]   #4방향
    yn = [0,0,1,-1]
    arr = [[0 for x in range(int(m))] for y in range(int(n))]   #2차원배열로 선언 
    bfs_ans = [[0 for x in range(int(m))] for y in range(int(n))]
    ids_ans = [[0 for x in range(int(m))] for y in range(int(n))]
    gbfs_ans = [[0 for x in range(int(m))] for y in range(int(n))]
    a_star_ans = [[0 for x in range(int(m))] for y in range(int(n))]

    i=0
    for x in inp:
        j=0
        for y in x:
            if y != '\n':
                arr[i][j] = int(y)   #입력받은 미로를 int형으로 변환시키며 배열에 저장
            j+=1
        i+=1
        
    #결과물을 출력을 위한 배열 초기화(현재 입력받은 미로)
    for i in range(int(m)):
        for j in range(int(n)):
            bfs_ans[i][j] = arr[i][j]
            ids_ans[i][j] = arr[i][j]
            gbfs_ans[i][j] = arr[i][j]
            a_star_ans[i][j] = arr[i][j]
            
    #시작점 부터 열쇠까지 탐색 후 방문노드 갯수와 길이를 저장 후, 열쇠부터 도착점 까지 탐색하여 방문노드 갯수와 길이를 추가 
    for i in range(int(m)):
        for j in range(int(n)):
            if arr[i][j] == 3:   #시작점 좌표 탐색 
                #bfs
                key = bfs(i,j,6)   #시작좌표와 키값을 넣고, 키의 좌표 탐색노드 갯수, 길이를 받아옴 
                bfs_time = key[2]
                bfs_length = key[3]
                ans = bfs(key[0],key[1],4)   #키의좌표와 종료값을 넣고, 도착좌표와 탐색노드 갯수, 길이를 받아옴
                bfs_time += ans[2]
                bfs_length += ans[3]
                #ids
                key = ids(i,j,6)
                ids_time = key[2]
                ids_length = key[3]
                ans = ids(key[0],key[1],4)
                ids_time += ans[2]
                ids_length += ans[3]
                #gbfs
                key = greedy_bfs(i,j,6)
                gbfs_time = key[2]
                gbfs_length = key[3]
                ans = greedy_bfs(key[0],key[1],4)
                gbfs_time += ans[2]
                gbfs_length += ans[3]
                #a_star
                key = a_star(i,j,6)
                a_star_time = key[2]
                a_star_length = key[3]
                ans = a_star(key[0],key[1],4)
                a_star_time += ans[2]
                a_star_length += ans[3]
                break
    #출력 
    output(k,bfs_time,bfs_length,"BFS",bfs_ans)
    output(k,ids_time,ids_length,"IDS",ids_ans)
    output(k,gbfs_time,gbfs_length,"GBFS",gbfs_ans)
    output(k,a_star_time,a_star_length,"A_star",a_star_ans)
#-----------------------------process

    
#main
i=0
while True:  #i를 증가 시키며 파일이 존재하지 않으면 종료
    i+=1
    try:
        f = open("Maze_%d.txt" % i, "r")   #Maze_1,2,3,... 파일 실행
    except FileNotFoundError:   #존재하지 않으면 프로그램 종료 
        break
    k,m,n = f.readline().split()   #k,m,n입력
    inp  = f.readlines()   #미로 입력 
    Maze(k,n,m,inp)   #Maze함수 실행 
