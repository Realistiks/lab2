print("Hello, World!")
name = "Кирилл Колесников"
print(f"Студент: {name}")
print("Дата: 2026-10-10")


def square(x: int) -> int:
    return x * x


number = 7
result = square(number)
print(f"Число: {number}")
print(f"Квадрат: {result}")


def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n.

    Факториал числа n (обозначается n!) — это произведение всех
    натуральных чисел от 1 до n. По определению 0! = 1.

    Args:
        n: Неотрицательное целое число.

    Returns:
        Факториал числа n.

    Raises:
        ValueError: Если n отрицательное.
        TypeError: Если n не целое число.

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
    """
    if not isinstance(n, int):
        raise TypeError(f"Ожидается int, получено {type(n).__name__}")
    if n < 0:
        raise ValueError(
            f"Факториал определён только для неотрицательных чисел, получено {n}"
        )

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(factorial(4))
