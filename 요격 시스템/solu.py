def solution(targets):
    ans = 0
    targets.sort(key = lambda x: x[1])
    
    st = 0
    ed = 0
    
    for i in range(len(targets)):
        tgt = targets[i]
        if tgt[0] >= ed:
            ans += 1
            ed = tgt[1]
            # st = tgt[0]
    
    return ans