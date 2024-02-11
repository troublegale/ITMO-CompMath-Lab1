# THIS ALL WAS A VERY BAD IDEA

# import math
#
#
# class Exponential:
#     def __init__(self, number: float):
#         number_str = normalize(number)
#         parts = number_str.split('.')
#         decimal_length = len(parts[1])
#         self.base = int(number * (10 ** decimal_length))
#         self.exp = decimal_length
#
#     def to_float(self) -> float:
#         f = float(self.base) / (10 ** self.exp)
#         if math.isclose(f, math.ceil(f)):
#             f = float(math.ceil(f))
#         elif math.isclose(f, math.floor(f)):
#             f = float(math.floor(f))
#         return f
#
#
# def normalize(number: float) -> str:
#     f = format(number, '.16f')
#     redundant = 0
#     for i in f[::-1]:
#         if i == '0':
#             redundant += 1
#         else:
#             break
#     return f[:-redundant] if redundant != 0 else f
#
#
# def __base_and_exp_to_exponential(base: int, exp: int) -> Exponential:
#     f = float(base) / (10 ** exp)
#     return Exponential(f)
#
#
# def exp_negative(e: Exponential):
#     return __base_and_exp_to_exponential(-e.base, e.exp)
#
#
# def exp_sum(e1: Exponential, e2: Exponential) -> Exponential:
#     a = e1.base if e1.exp > e2.exp else e1.base * (10 ** (e2.exp - e1.exp))
#     b = e2.base if e2.exp > e1.exp else e2.base * (10 ** (e1.exp - e2.exp))
#     exp = max(e1.exp, e2.exp)
#     e_sum = __base_and_exp_to_exponential(a + b, exp)
#     return e_sum
#
#
# def exp_product(e1: Exponential, e2: Exponential) -> Exponential:
#     return __base_and_exp_to_exponential(e1.base * e2.base, e1.exp + e2.exp)
#
#
# def exp_quotient(e1: Exponential, e2: Exponential) -> Exponential:
#     float_base = float(e1.base) / float(e2.base)
#     e = Exponential(float_base)
#     e.exp += e1.exp - e2.exp
#     return e
