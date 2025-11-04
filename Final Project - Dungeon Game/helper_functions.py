import math

def easeOutCirc(x: float) -> float:
    return math.sqrt(1 - math.pow(x - 1, 2))