from typing import Iterable

import matplotlib.pyplot as plt
from prettytable import PrettyTable


def __render_table(
    table: PrettyTable,
    x_values: Iterable[float],
    picard: Iterable[list[float]],
    euler: Iterable[float],
    runge_kutta: Iterable[float],
):
    k = 0
    for (
        x,
        p1,
        p2,
        p3,
        p4,
        e,
        rk,
    ) in zip(x_values, *picard, euler, runge_kutta):
        if k % 500 == 0:
            table.add_row(
                [
                    f"{x:10.5f}",
                    f"{p1:20.5f}",
                    f"{p2:20.5f}",
                    f"{p3:20.5f}",
                    f"{p4:20.5f}",
                    f"{e:20.5f}",
                    f"{rk:20.5f}",
                ]
            )
        k += 1


def _make_x(x: list[float]) -> list[float]:
    return list(reversed(list(map(lambda val: -val, x)))) + x


def _make_picard(
    picard: tuple[list[float], list[float], list[float], list[float]]
) -> tuple[list[float], list[float], list[float], list[float]]:
    return tuple(_make_smt(pr) for pr in picard)


def _make_smt(lst: list[float]) -> list[float]:
    return list(reversed(lst)) + lst


def render_graph(
    x_values: list[float],
    picard_res: tuple[list[float], list[float], list[float], list[float]],
    euler_res: list[float],
    runge_kutta_res: list[float],
) -> None:
    plt.clf()

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(axis="y", color="gray", linewidth=0.2)

    x = _make_x(x_values)

    f1, f2, f3, f4 = _make_picard(picard_res)
    plt.plot(x, f1, label="Picard (1st)")
    plt.plot(x, f2, label="Picard (2nd)")
    plt.plot(x, f3, label="Picard (3rd)")
    plt.plot(x, f4, label="Picard (4th)")

    f5 = _make_smt(euler_res)
    plt.plot(x, f5, label="Euler")

    f6 = _make_smt(runge_kutta_res)
    plt.plot(x, f6, label="Runge-Kutta")

    plt.legend()
    plt.savefig("measures.png")
    plt.show()


def render_table(
    x_values: list[float],
    picard_res: tuple[list[float], list[float], list[float], list[float]],
    euler_res: list[float],
    runge_kutta_res: list[float],
):
    t = PrettyTable(
        [
            "X",
            "Picard (1st)",
            "Picard (2nd)",
            "Picard (3rd)",
            "Picard (4th)",
            "Euler",
            "Runge-Kutta",
        ]
    )

    __render_table(
        table=t,
        x_values=x_values,
        picard=picard_res,
        euler=euler_res,
        runge_kutta=runge_kutta_res,
    )

    print(t)
