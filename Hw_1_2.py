from collections import deque

def is_palindrome(input_str):
    input_str = input_str.lower().replace(" ", "")
    char_queue = deque(input_str)
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

input_string = input("Введіть текст для перевірки: ")
result = is_palindrome(input_string)

if result:
    print(f"Рядок '{input_string}' є паліндромом.")
else:
    print(f"Рядок '{input_string}' не є паліндромом.")