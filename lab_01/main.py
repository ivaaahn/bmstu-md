import math

import output
import cauchy
from misc import *


X_START = 0.0
X_END = 2.0
Y_START = 0.0
STEP = 1e-4


def main():
    x_start, x_end = X_START, X_END
    y_start = Y_START
    step = STEP

    num_of_steps: int = math.ceil(abs(x_end - x_start) / step) + 1

    picard_res = cauchy.picard(x_start, h=step, n=num_of_steps)
    euler_res = cauchy.euler(x_start, y_start, h=step, n=num_of_steps)
    runge_kutta_res = cauchy.runge_kutta(
        x_start, y_start, a=0.5, h=step, n=num_of_steps
    )

    x_values = make_x_values_to_print(x_start, step, num_of_steps)

    output.render_table(x_values, picard_res, euler_res, runge_kutta_res)
    output.render_graph(x_values, picard_res, euler_res, runge_kutta_res)


if __name__ == "__main__":
    main()
