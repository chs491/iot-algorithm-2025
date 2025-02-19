# hbc.py
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    # 그래프 출력시 정점표시하는 함수
def printGraph(g): # g : Graph 객체 매개변수
    global nameAry # nameAry의 데이터를 함수 내에서 변경하겠다! 변경할 일이 없으면 생략!!

    print('\t', end = '\t')
    for v in range(g.SIZE):
        print(nameAry[v], end = '\t')
    print()

    for row in range(g.SIZE):
        print(nameAry[row], end = '\t\t') # 행마다 정점이름 추가
        for col in range(g.SIZE):
            print(f'{g.graph[row][col]:>2d}', end = '\t')
        print() # 열을 다 표현하면 다음 행으로 한줄 내림 

    print()  

G = None    
nameAry = [['GS25', 30],['CU', 60],['seven11', 10],['Ministop', 90],['emart24', 40]]
GS25, CU, seven11, Ministop, emart24 = 0,1,2,3,4

SIZE = 5
G = Graph(SIZE)
G.graph[GS25][CU] = 1; G.graph[GS25][seven11] = 1
G.graph[CU][GS25] = 1; G.graph[CU][seven11] = 1; G.graph[CU][Ministop] = 1
G.graph[seven11][GS25] = 1; G.graph[seven11][CU] = 1; G.graph[seven11][Ministop] = 1
G.graph[Ministop][seven11] = 1; G.graph[Ministop][CU] = 1; G.graph[Ministop][emart24] = 1
G.graph[emart24][Ministop] = 1

print('## 편의점 그래프 ##')
printGraph(G)

stack = []
visitedAry = []

current = 0
maxStore = current
maxCount = nameAry[current][1]
stack.append(current) 
visitedAry.append(current) 

while len(stack) != 0: 
    next = None
    for vertex in range(SIZE):
        if G.graph[current][vertex] == 1: 
            if vertex in visitedAry: 
                continue
            else:
                next = vertex 
                break
    if next != None: 
        current = next
        stack.append(current)
        visitedAry.append(current)
        if nameAry[current][1] > maxCount:
            maxCount = nameAry[current][1]
            maxStore = current
    else:
        current = stack.pop() 

print(f'허니버터칩 최대 보유 편의점(보유 개수) --> {nameAry[maxStore][0]}({nameAry[maxStore][1]})')            
    