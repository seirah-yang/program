# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

# 문자열 치환과 패턴 검사(String Replacement & Pattern Check)
# 같은 발음이 연속되지 않는지” 확인하는 ##문자열 처리 문제## 

# 1. 발음 가능한 기본 단위: ["aya", "ye", "woo", "ma"]
# 2. 각 단어마다 반복문으로 확인 -> 조건 = 허용된 조합으로만 구성: 문자열 전체가 위 단어들의 반복으로만 이루어져야 함.
# 3. 연속패턴(P*2) 발견시 중단(break) -> 같은 발음 연속 금지: "yeye", "woowoo" → ❌ 불가능 (같은 단위가 연속으로 나오면 안 됨)
# 4. 패턴을 ''로 치환하면서 제거
# 5. 남은 문자열이 비어 있다면 모두 허용된 발음으로 구성 -> 카운트 +1 

def solution(babbling):
  ans = 0
  possible = []
  for word in :
    for p in possible
      if (p *2) in word: 
        break
      word = word.replace(p, '')
    else : 
       if word.strp() == '':
          ans +=1
  return ans
