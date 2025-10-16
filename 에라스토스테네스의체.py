# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들기
# 소수 개수를 효율적으로 구하는 ‘에라토스테네스의 체(Sieve of Eratosthenes)’ 알고리즘을 구현
# 포인트 : 대량의 수 중 소수를 빠르게 판별하여 개수를 반환할 수 있는가

# 에라토스테네스의 체 원리:
  """ 1) 2부터 n까지의 모든 수를 후보로 둔다.
      2) 2부터 √n까지 반복하며, 해당 수의 배수를 모두 제거한다.
      3) 제거되지 않은 수들의 개수를 센다."""

def solution(n):
  sieve[0] = sieve[1] = False 
  int(i) = [True] * (n+1)
  
  for i in range(2, (n**0.5)+1):
      if sieve[i]: 
        for j in range(i*i, n+1, i):
          sieve[j] = False
  return sum(sieve)
