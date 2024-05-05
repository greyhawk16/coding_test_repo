def solution(prices):
	# 1. 변수 초기화
    n = len(prices)
    ans = [0 for _ in range(n)]
    stk = []
    
    # 2. 가격이 떨어질 때 까지의 시간 구하기
    for i in range(n):
        while stk and prices[stk[-1]] > prices[i]:
            post = stk.pop()
            ans[post] = i - post
        else:
            stk.append(i)
    
    # 3. 가격이 한번도 떨어지지 않은 경우
    for i in stk:
        ans[i] = n - i - 1
    
    return ans


a = [1, 2, 3, 2, 3]
print(solution(a))