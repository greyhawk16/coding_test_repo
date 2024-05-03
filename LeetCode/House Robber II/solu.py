class Solution:
    def rob(self, nums: list[int]) -> int:
        # 1. 집들의 개수가 적을 경우
        if len(nums) == 1:
            return nums[0]

        elif len(nums) <= 3:
            return max(nums)

        # 2. DP 탐색
        else:
            # 1) 변수 초기화
            n = len(nums)
            dp1 = [0 for _ in range(n)]     # 1번 집 털기
            dp2 = [0 for _ in range(n)]     # 2번 집 털기

            dp1[0] = nums[0]
            dp2[1] = nums[1]

            # 2) 1번째 집부터 털 때
            for i in range(1, n-1):
                not_rob = dp1[i-1]			# 현재 집을 털지 않을 때 얻는 돈
                rob = dp1[i-2] + nums[i]		# 현재 집을 털 때 얻는 돈
                dp1[i] = max(rob, not_rob)		# 최댓값을 dp1에 반영

            # 3) 2번째 집부터 털 때
            for i in range(2, n):
                not_rob = dp2[i-1]			# 현재 집을 털지 않을 때 얻는 돈
                rob = dp2[i-2] + nums[i]		# 현재 집을 털 때 얻는 돈
                dp2[i] = max(rob, not_rob)		# 최댓값을 dp2에 반영

            # 4) 답 구하기
            fst = max(dp1)		# 1번째 집부터 털 때 올릴 수 있는 최대 성과
            sec = max(dp2)		# 2번째 집부터 털 때 올릴 수 있는 최대 성과

            ans = max(fst, sec)		# 더 큰 값을 반환
            return ans