class Exponential:
    def __init__(self, number: float):
        decimal_length = len(str(float(number)).split(".")[1])
        self.base = int(number * (10 ** decimal_length))
        self.exp = decimal_length

    def to_float(self) -> float:
        return float(self.base) / (10 ** self.exp)


def __base_and_exp_to_exponential(base: int, exp: int) -> 'Exponential':
    f = float(base) / (10 ** exp)
    return Exponential(f)


def exp_sum(e1: 'Exponential', e2: 'Exponential') -> 'Exponential':
    a = e1.base if e1.exp > e2.exp else e1.base * (10 ** (e2.exp - e1.exp))
    b = e2.base if e2.exp > e1.exp else e2.base * (10 ** (e1.exp - e2.exp))
    exp = max(e1.exp, e2.exp)
    e_sum = __base_and_exp_to_exponential(a + b, exp)
    return e_sum


def exp_product(e1: 'Exponential', e2: 'Exponential') -> 'Exponential':
    return __base_and_exp_to_exponential(e1.base * e2.base, e1.exp + e2.exp)
