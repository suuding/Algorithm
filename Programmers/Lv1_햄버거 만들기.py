# 스택 사용 
def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient :
        stack.append(i)
        if stack[-4:]==[1,2,3,1] :
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer+=1
    
    return answer
