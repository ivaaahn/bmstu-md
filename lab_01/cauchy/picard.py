__all__ = ("picard",)


def approx1(x: float) -> float:
    return x * x * x / 3


def approx2(x: float) -> float:
    return approx1(x) + x**7 / 63


def approx3(x: float) -> float:
    return approx2(x) + 2 * x**11 / 2079 + x**15 / 59535


def approx4(x: float) -> float:
    return (
        approx2(x)
        + 2 * x**11 / 2079
        + 13 * x**15 / 218295
        + 82 * x**19 / 37328445
        + 662 * x**23 / 10438212015
        + 4 * x**27 / 3341878155
        + x**31 / 109876902975
    )


def picard(
    x0: float, h: float, n: int
) -> tuple[list[float], list[float], list[float], list[float]]:
    res = (
        [],
        [],
        [],
        [],
    )

    for i in range(n):
        res[0].append(approx1(x0))
        res[1].append(approx2(x0))
        res[2].append(approx3(x0))
        res[3].append(approx4(x0))

        x0 += h

    return res
