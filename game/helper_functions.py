import math

def ease_out_circ(x: float) -> float:
    return math.sqrt(1 - math.pow(x - 1, 2))