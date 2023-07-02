def is_balanced_string(string):
    stack = []

    for char in string:
        # 왼쪽 괄호인 경우
        if char in '([{':
            # 스택에 추가
            stack.append(char)
        # 오른쪽 괄호인 경우

        elif char in ')]}':
            # 스택이 비어있으면 짝이 없는 경우이므로 "no" 반환
            if not stack:
                return "no"
            # 스택의 가장 위에 있는 괄호를 꺼내옴
            top = stack.pop()

            # 괄호의 짝이 맞지 않는 경우이므로 "no" 반환
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return "no"

    if stack: # 순회 후에도 스택에 괄호가 남아있으면 짝이 맞지 않는 경우이므로 "no" 반환
        return "no"
    else:
        return "yes" # 모든 괄호의 짝이 맞아 균형이 잘 이루어진 경우 "yes" 반환


# 입력 예시
inputs = []
while True:
    string = input()
    if string == '.':
        break
    inputs.append(string)

# 각 입력에 대한 결과 출력
for string in inputs:
    result = is_balanced_string(string)
    print(result)
