string = input()
num = int(input())
print(string.count('a')*(num//len(string)) + (string[:num % len(string)].count('a')))
