# import os

# def makeFileList(folderName):
#     fnameAry = []
#     for dirName, subDirList, fnames in os.walk(folderName):
#         for fname in fnames:
#             fnameAry.append(fname)
#     return fnameAry

# def sortInsertion(ary):
#     n = len(ary)
#     for end in range(1,n): 
#         for cur in range(end, 0, -1): 
#             if ary[cur - 1] > ary[cur]:
#                 ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
#         print(f'정렬 중 -> {ary}')        
#     return ary      

# def sortInsertion(ary):
#     n = len(ary)
#     for end in range(1,n): 
#         for cur in range(end, 0, -1): 
#             if ary[cur - 1][1] > ary[cur][1]:
#                 ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
#         print(f'정렬 중 -> {ary}')        
#     return ary   

# fileAry = []

# fileAry = makeFileList('C:\Source\iot-prev-story-2025\day02')
# fileAry = sortInsertion(fileAry)
# print(f'파일명 역순 정렬 --> {fileAry}')

# scoreAry = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

# print(f'정렬 전 -> {scoreAry}')
# scoreAry = sortInsertion(scoreAry)
# print(f'정렬 후 -> {scoreAry}')
# print('## 성적별 조 편성표 ##')
# for i in range(len(scoreAry)//2):
#     print(f'{scoreAry[i][0]} : {scoreAry[len(scoreAry)-1-i][0]}')

def sortSelection(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for j in range(i+1, n):
            if ary[minIdx] > ary[j]:
                minIdx = j

        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

        print(f'정렬 중 --> {ary}')

    return ary   

ary2 = [[55,33,250,44], [88,1,67,23], [199,222,38,47], [155,145,20,99]]
ary1 = []

for i in range(len(ary2)):
    for j in range(len(ary2[i])):
        ary1.append(ary2[i][j])

print(f'1차원 변경 후, 정렬 전 --> {ary1}')
ary1 = sortSelection(ary1)
print(f'1차원 변경 후, 정렬 후 --> {ary1}') 
print(f'중앙값 --> {ary1[len(ary1)//2]}')    
