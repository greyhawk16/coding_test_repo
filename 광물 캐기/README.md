# 키워드: 
- 정렬

# 풀이

1. 곡괭이는 5개의 광물을 캘 수 있다. 
   주어진 곡괭이로 캘 수 있는 광물의 수 `sum(picks) * 5` 보다 주어진 광물 수 `len(minerals)`가 많다면, 곡괭이로 캘 수 있는 만큼의 광물 `minerals[:sum(picks)*5]` 만 고려한다.

2. 광물들을 5개 단위로 끊어서, 한 단위 당 다이아몬드, 철, 돌의 개수를 센다.

3. 피로도가 가장 높은 광물 묶음이 맨 앞에 오도록 정렬

4. 정렬한 광물 묶음을 다이아 -> 철 -> 돌 순으로 캔다.
   여기서 내구도가 가장 높은 곡괭이부터 사용하면, 피로도를 최소로 줄일 수 있다.
   


# 참고 사이트
- https://yunchan97.tistory.com/48 