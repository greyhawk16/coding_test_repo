def solution(phone_book):   
    # 1. 초기화 및 탐색 준비
    ans = True
    dct = dict()    # 딕셔너리 선언

    for p in phone_book:
        dct[p] = True  # 현재 전화번호를 딕셔너리에 key로 집어넣기
    
    # 2. 접두어 탐색
    for p in phone_book:
        header = ''          # 접두어 초기화
        for n in p:
            header += n      # 접두어 생성
            if header in dct.keys() and header != p:  # 접두어가 주어진 전화번호 중 하나라면
                ans = False  
                return ans

    return ans