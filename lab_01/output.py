import matplotlib.pyplot as plt
from prettytable import PrettyTable


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

    x = x_values

    f1, f2, f3, f4 = picard_res
    plt.plot(x, f1, label="Picard (1st)")
    plt.plot(x, f2, label="Picard (2nd)")
    plt.plot(x, f3, label="Picard (3rd)")
    plt.plot(x, f4, label="Picard (4th)")

    f5 = euler_res
    plt.plot(x, f5, label="Euler")

    f6 = runge_kutta_res
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

    k = 0
    for (
        x,
        p1,
        p2,
        p3,
        p4,
        e,
        rk,
    ) in zip(x_values, *picard_res, euler_res, runge_kutta_res):
        if k % 500 == 0:
            t.add_row(
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

    print(t)
