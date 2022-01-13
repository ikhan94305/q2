def solution(numbers):
    check = [0,1,2,3,4,5,6,7,8,9]
    answer = 0
    for i in check:
        if i not in numbers:
            answer += i
    return answer

numbers = [5,8,4,0,6,7,9]
answer = solution(numbers)
print(answer)
