import sys

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().rstrip()[1:-1].split(',')))
    
    if len(arr) <= 1:
        print("error")
        continue
        
    reverse_flag = False
    front, rear = 0, 0
    
    for op in p:
        if op == 'R':
            reverse_flag = not reverse_flag
        elif op == 'D':
            if front == rear:
                print("error")
                break
            else:
                if reverse_flag:
                    rear += 1
                else:
                    front += 1
    
    else:
        if reverse_flag:
            arr = arr[front:len(arr) - rear][::-1]
        else:
            arr = arr[front:len(arr) - rear]
        print('[{}]'.format(','.join(map(str, arr))))
