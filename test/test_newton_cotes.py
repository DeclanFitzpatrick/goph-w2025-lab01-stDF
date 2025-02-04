import numpy as np
from goph420_lab01.intergration import (
    integrate_newton_trap,
)

def test_newton_trap():
    x = np.linespace(-2.0, 5.0)
    f0 = 5.0 * np.ones_like(x)
    f1 = -2.5 + 0.6 * x

    I0_exp = f0[0] * (x[-1] - x[0])
    I0_act_2 = integrate_newton_trap(
        [x[0]], x[-1],
        [f0[0]], f0[-1],
    )
    I0_act_all = integrate_newton_trap(x, f0)
    print("Testing Trapazoid rule: ")
    print(f"f(x) = {f0[0]} from x={x[0]} to x = {x[-1]}")
    print(f"Expected: {I0_exp}")
    print(f"Actual (2 data pts): {I0_act_2}")
    print(f"Actual ({len(x)} data pts): {I0_act_all}")


if __name__ == "__main__":
    test_newton_trap()