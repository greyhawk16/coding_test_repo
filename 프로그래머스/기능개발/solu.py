def solution(progresses, speeds):
    # 1. 변수 준비
    # trace[i]: [x일, x일에_배포하는_기능_수], i != x
    trace = []
    n = len(progresses)
    
    # 2. 각 기능 별 순회
    for i in range(n):
        # 1) 잔여시간 구하기
        prog = progresses[i]
        sped = speeds[i]
        remain = -((prog - 100) // sped)    # 잔여 일자 구하기
        
        # 2) 기능이 순서대로 완성되는 경우
        if not trace or trace[-1][0] < remain:  
            trace.append([remain, 1])     # 대기없이 바로 배포
            
        # 3) 선행기능보다, 현재 기능이 빨리 완성되는 경우
        else:   
            trace[-1][1] += 1     # 이전 기능이 완성될 때 같이 배포 -> 배포할 기능 수 + 1
    
    # 3. 정답 반환
    ans = [i[1] for i in trace]
    return ans