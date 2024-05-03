'''
    - 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/176962
    - 참고 풀이: https://yunchan97.tistory.com/48 
'''


def solution(picks, minerals):

    # 주어진 광물의 수가 곡괭이로 캘 수 있는 것보다 많다면
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks)*5]  # 곡괭이 수의 5배 만큼의 광물만 고려
    
    mineral_5_set = [[0, 0, 0] for _ in range(len(minerals)//5 + 1)]  # 광물 목록을 5개 단위로 끊기
    
    for i in range(len(minerals)):         # 5덩이 당 다이아, 철, 돌 별 개수 세기
        if minerals[i] == "diamond":
            mineral_5_set[i//5][0] += 1
        elif minerals[i] == "iron":
            mineral_5_set[i//5][1] += 1
        else:
            mineral_5_set[i//5][2] += 1
    
    mineral_5_set = sorted(mineral_5_set, key = lambda x:(-x[0], -x[1], -x[2]))   # 피로도 기준, 내림차순 정렬
    ans = 0     # 필요한 최소 내구도
    
    for i in mineral_5_set:
        da, ir, st = i
        
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:     # 다이아 곡괭이
                picks[j] -= 1
                ans += da + ir + st
                break
            elif picks[j] > 0 and j == 1:   # 철 곡괭이
                picks[j] -= 1
                ans += (5 * da + ir + st)
                break
            elif picks[j] > 0 and j == 2:   # 돌 곡괭이
                picks[j] -= 1
                ans += (25 * da + 5 * ir + st)
                break
                
    return ans