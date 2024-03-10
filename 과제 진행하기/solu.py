'''
    - 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/176962
    
    - 참고 풀이: https://velog.io/@yeomja99/알고리즘-문제-풀이파이썬-프로그래머스-과제-진행하기
'''

def convert_time(s):    # 시간을 분 단위로 변환
    hh, mm = map(int, s.split(':'))
    return hh * 60 + mm


def solution(plans):
    ans = []
    
    for i in range(len(plans)):
        # 1. 시간대를 분 단위로 통일
        _, st, _ = plans[i]  
        st = convert_time(st)
        plans[i][1] = st
        plans[i][2] = int(plans[i][2])
        
    # 2. 시작 시간 순서대로 정렬
    plans.sort(key = lambda x:x[1])   
    stk = []    # 가장 최근에 들어온 과제부터 실행 -> 스택 구조 활용
    
    # 3. 
    for i in range(len(plans)):
        if i == len(plans) - 1:    # i.
            stk.append(plans[i])
            break
        
        task, st, dur = plans[i]     # 현재 보는 과제
        _, nex_st, _ = plans[i+1]    # 다음에 봐야 할 과제
        
        if st + dur <= nex_st:       # 다음 과제를 시작하기 전까지, 지금 보는 과제를 끝낼 수 있다면
            ans.append(task)         # ans에 과제명 추가
            temp_time = nex_st - (st + dur)       # 다음 과제를 시작하기 전까지 남은 시간
            
            while temp_time != 0 and stk:         # 시간이 남았고, 아직 못 끝낸 과제들이 있다면
                tmp_task, tmp_st, tmp_dur = stk.pop()   # 가장 최근에 못끝낸 과제 정보
                if temp_time >= tmp_dur:                # 그 과제를 남은 시간동안 끝낼 수 있다면
                    ans.append(tmp_task)                      # ans에 추가
                    temp_time -= tmp_dur                      # 남은 시간에서, 과제에 소모되는 시간만큼 차감
                else:
                    stk.append([tmp_task, tmp_st, tmp_dur - temp_time])     # 남은 시간만큼 차감 후, 스택에 다시 넣기
                    temp_time = 0                                           # 남은 시간 초기화
                    
        else:      # ii. 다음 과제를 시작하기 전까지, 현재 과제를 끝내지 못하면
            plans[i][2] = dur - (nex_st - st)     # 소모시간에서, 현재 ~ 다음과제 시작하는 시간차 만큼 차감
            stk.append(plans[i])                  # 스택에 현재 과제 추가
    
    # 4. 끝내지 못한 과제 처리
    while stk:
        task, _, _ = stk.pop()      # 가장 먼저 끝내는 과제
        ans.append(task)               # ans에 추가
    
    return ans