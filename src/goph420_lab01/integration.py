import numpy as np

def integrate_newton(x, f, alg="trap"):
    if alg.strip().lower() == "trap":
        return integrate_newton_trap(x, f)
    # elif alg.strip().lower() == "simp":
        # return integrate_newton_simp(x, f)
    
def integrate_newton_trap(x, f):
    """Intergrate using trapezoid rule.
    |
    Parameters
    ----------
    x : array_like
        The independent coordinate data.
    f : array_like
        The dependent variable
        Should have same shape and length as x
    |
    Return
    ------
    float

    Raises
    ------
    Value Error
        If x and f data do not have the same length.
    |
    Notes
    -----
    we assume constant step size in x
    |
    """
    x = np.array(x).flatten()
    f = np.array(f).flatten()
    if len(x) != len(f):
        raise ValueError(f"len(x) is (len(x)), len(f) is {len(f)}, should be equal")
    dx = x[1] - x[0]
    return 0.5 * dx * (f[0] + 2 * np.sum(f[1:-1]) + f[-1])
    