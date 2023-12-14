def greet(name: str, age: int) -> str:
    return f'hello, {name}! You are {age} years old'
def say_hello(to):
    print(f'안녕,  {to}?')
def say_goodbye(to):
    print(f'또 만나, {to}!')
if __name__ == '__main__':
    say_hello('파이썬')
    say_goodbye('나도코딩')