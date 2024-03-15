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
        plans[i][1] = st                 # 1. 시간대를 분 단위로 통일
        plans[i][2] = int(plans[i][2])   # 소모시간은 정수로 변환
        
    # 2. 시작 시간 순서대로 정렬
    plans.sort(key = lambda x:x[1])   
    stk = []    # 가장 최근에 들어온 과제부터 실행해야 하므로, LIFO인 스택 구조 활용
    
       # 3. 과제 순회
    for i in range(len(plans)):
    
    	# 1) 마지막 과제라면
        if i == len(plans) - 1:   
            stk.append(plans[i])
            break
            
        # 2) 현재 과제와, 바로 다음에 봐야 할 과제 정보 가져오기
        task, st, dur = plans[i]     # 현재 보는 과제
        _, nex_st, _ = plans[i+1]    # 다음에 봐야 할 과제
        
        # 3) 다음 과제를 시작하기 전까지, 지금 보는 과제를 끝낼 수 있다면
        if st + dur <= nex_st:       
        
            ans.append(task)                    # ans에 과제명 추가
            temp_time = nex_st - (st + dur)     # 다음 과제를 시작하기 전까지 남은 시간
            
            while temp_time != 0 and stk:       # 시간이 남았고, 아직 못 끝낸 과제들이 있다면
                tmp_task, tmp_st, tmp_dur = stk.pop()   # 가장 최근에 못끝낸 과제 정보
                
                # (1) 시간이 남았고, 아직 못 끝낸 과제들이 있다면
                if temp_time >= tmp_dur:                
                    ans.append(tmp_task)       # ans에 추가
                    temp_time -= tmp_dur       # 남은 시간에서, 과제에 소모되는 시간만큼 차감
                
                # (2) 다 끝내기엔 시간이 부족한 경우
                else:
                    stk.append([tmp_task, tmp_st, tmp_dur - temp_time])  # 스택에 다시 넣기
                    temp_time = 0                                        # 남은 시간 초기화
        
        # 4) 다음 과제를 시작하기 전까지, 현재 과제를 끝내지 못하면
        else:      
            plans[i][2] = dur - (nex_st - st)     # 현재 ~ 다음과제 시작하는 시간차만큼 소모시간 차감
            stk.append(plans[i])                  # 스택에 현재 과제 추가
    
    # 4. 끝내지 못한 과제 처리
    while stk:
        task, _, _ = stk.pop()      # 가장 먼저 끝내는 과제
        ans.append(task)               # ans에 추가
    
    return ans