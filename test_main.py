def test_compose_pipeline():
    from main import compose_pipeline

    def add1(x):
        return x + 1

    def square(x):
        return x * x

    pipeline = compose_pipeline(add1, square)
    assert pipeline(2) == 9  # (2 + 1) ^ 2 = 9
    assert pipeline(3) == 16  # (3 + 1) ^ 2 = 16

    pipeline2 = compose_pipeline(square, add1)
    assert pipeline2(2) == 5  # 2^2 + 1 = 5
    assert pipeline2(3) == 10  # 3^2 + 1 = 10

    def halve(x):
        return x / 2

    pipeline3 = compose_pipeline(add1, square, halve)
    assert pipeline3(3) == 8.0  # ((3 + 1)^2) / 2 = 8.0

    pipeline4 = compose_pipeline()
    assert pipeline4(3) == 3
    assert pipeline4(-1) == -1

    pipeline5 = compose_pipeline(add1)
    assert pipeline5(0) == 1
    assert pipeline5(5) == 6


def test_power_sequence():
    from main import power_sequence

    assert power_sequence(2, 4) == 30  # 2^1 + 2^2 + 2^3 + 2^4 = 30
    assert power_sequence(2, 1) == 2  # 2^1 = 2

    assert power_sequence(3, 3) == 39  # 3^1 + 3^2 + 3^3 = 39
    assert power_sequence(3, 2) == 12  # 3^1 + 3^2 = 12

    assert power_sequence(5, 2) == 30  # 5^1 + 5^2 = 30
    assert power_sequence(5, 3) == 155  # 5^1 + 5^2 + 5^3 = 155

    assert power_sequence(10, 1) == 10  # 10^1 = 10
    assert power_sequence(10, 3) == 1110  # 10^1 + 10^2 + 10^3 = 1110

    assert power_sequence(2, 10) == 2046  # Sum of 2^1 to 2^10
