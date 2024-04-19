def solution(N, number):
    ans = -1
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        case = dp[i]
        case.add(int(str(N) * i))
        
        for j in range(1, i):         # j:   N을 몇번 사용할 지
            for k in dp[j]:           # k:   j개의 N으로 만들 수 있는 수들
                for l in dp[i-j]:     # l:   이전에 파악한 수들 (j-1개의 N으로 만들 수 있는 수, ... , 1개의 N으로 만들 수 있는 수 )
                    case.add(k + l)
                    case.add(k - l)
                    case.add(k * l)
                    if k * l != 0 :   # k, l이 둘 다 0이 아니면
                        case.add(k // l)
        
        if number in case:
            ans = i
            break
    
    return ans


# N = 5
# number = 12
# print(solution(N, number))