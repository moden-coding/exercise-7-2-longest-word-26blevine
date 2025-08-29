# Write your solution here
def longest(strings : list):
    biggest = ""
    for str in strings:
        if len(str) > len(biggest):
            biggest = str
    return biggest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))