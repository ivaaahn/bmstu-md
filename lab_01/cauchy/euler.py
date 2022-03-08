from .misc import equation


__all__ = ("euler",)


def euler(x0: float, y0: float, h: float, n: int) -> list[float]:
    res = []

    for i in range(n):
        res.append(y0)
        y0 += h * equation(x0, y0)
        x0 += h

    return res
