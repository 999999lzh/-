def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return a

def main():
    try:
        n = int(input("输入斐波那契数列项数："))
        if n < 0:
            print("输入错误请输入正整数")
        else:
            result = fibonacci(n)
            print(f"斐波那契数列的第{n}项是：{result}")
    except ValueError:
        print("请输入有效的整数")

if __name__ == "__main__":
    main()