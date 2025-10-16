# list slicing: array[i-1:j] -> i번째부터 j번째까지의 구간 추출 
# Sorting: sorted() 함수를 사용하여 오름차순 정렬 
# Indexing: K-1번째 원소 접근 
# Iteration: Commands에 대해 위 과정을 반복 수행 

# array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면, array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
def solution(array, commands):
  ans = []
  for lst in array[i-1:j]:
    s_lst = sorted(lst)
    ans.append(s_lst[k-1])
  return ans

# 내가 잘 발생시키는 ❌ 오류 3가지 #
""" range[i-1,j] → range()는 함수가 아니라 리스트 슬라이싱이 필요합니다.
👉 array[i-1:j]로 써야 합니다.

for lst in range[i-1,j]: → i, j, k는 commands 안에 들어있기 때문에 루프에서 꺼내야 합니다.
👉 for i, j, k in commands: 형태로 써야 합니다.

lst는 숫자가 아니라 슬라이싱된 리스트여야 합니다.
현재 구조로는 각 명령마다 슬라이싱이 제대로 되지 않습니다."""

def solution(array, commands): 
  ans = []
  for i, j, k in commands:       # 4. 반복 : 명령마다 반복수행 
    lst = array[i-1:j]         # 1. 슬라이싱 : 부분 구간 추출 
    s_lst = sorted(lst)        # 2. 오름차순 정렬
    ans.append(s_lst[k-1])     # 3. 인덱싱 : k번째 원소접근 
  return ans  
