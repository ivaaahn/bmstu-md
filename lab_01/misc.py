def make_x_values_to_print(
    x_start: float, step: float, num_of_steps: int
) -> list[float]:
    xn = x_start
    x_values = []
    for i in range(num_of_steps):
        x_values.append(xn)
        xn += step

    return x_values
