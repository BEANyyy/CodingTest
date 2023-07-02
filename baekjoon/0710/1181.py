# 단어를 저장할 배열
words = []

# 입력받기
n = int(input())

for i in range(n):
    word = input()
    words.append(word)

#중복값 제거
sorted_words = list(set(words))

# 사전순 정렬
sorted_words.sort()

# 글자 수에 맞춰 1차 정렬
sorted_words.sort(key=len)

# 출력
for word in sorted_words:
    print(word)
    
