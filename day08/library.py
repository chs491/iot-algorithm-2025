from operator import itemgetter

def makeIndex(ary, pos):
    beforeAry = []
    index = 0
    for data in ary:
        beforeAry.append((data[pos], index))
        index += 1

    sortedAry = sorted(beforeAry, key = itemgetter(0))
    return sortedAry

def bookSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary) - 1 # 리스트 마지막 인덱스

    while (start <= end): # 시작이 끝보다 커지면 검색실패
        mid = (start + end) // 2
        if fData == ary[mid][0]:
            return ary[mid][1]
        elif fData > ary[mid][0]:
            start = mid + 1 # 뒤쪽에 데이터가 있다.
        else:
            end = mid - 1  # 앞쪽에 데이터가 있다.
    return pos    

bookAry = [['어린왕자', '생텍쥐베리'],['이방인', '까뮈'],
           ['부활', '톨스토이'],['신곡', '단테'],['돈키호테', '세르반테스'],
           ['동물농장', '조지오웰'],['데미안', '헤르만헤세'],['파우스트', '괴테'], ['대지', '펄벅']]
nameIndex = []
authIndex = []

print(f'# 책장의 도서 ==> {bookAry}')
nameIndex = makeIndex(bookAry, 0)
print(f'# 도서명 색인표 ==> {nameIndex}')
authIndex = makeIndex(bookAry, 1)
print(f'# 작가명 색인표 ==> {authIndex}')

findName = '신곡'
findPos = bookSearch(nameIndex, findName)
if findPos != -1:
    print(f'{findName}의 작가는 {bookAry[findPos][1]}입니다.')
else:
    print(f'{findName}책은 없습니다.')

findName = '채식주의자'
findPos = bookSearch(nameIndex, findName)
if findPos != -1:
    print(f'{findName}의 작가는 {bookAry[findPos][1]}입니다.')
else:
    print(f'{findName}책은 없습니다.')

