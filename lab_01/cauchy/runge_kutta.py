from .misc import equation

__all__ = ("runge_kutta",)


def runge_kutta(x0: float, y0: float, a: float, h: float, n: int) -> list[float]:
    res = []

    g = equation

    for i in range(n):
        res.append(y0)

        x_ = x0 + h / (2 * a)
        y_ = y0 + h * g(x0, y0) / (2 * a)

        y0 += h * ((1 - a) * g(x0, y0) + a * g(x_, y_))

        x0 += h

    return res
