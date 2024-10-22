from modul_4_1_fake_math import divide as zero_divide
from modul_4_1_true_math import divide as inf_divide

# test
result1 = zero_divide(69, 3)
result2 = zero_divide(5, 0)
result3 = inf_divide(13, 5)
result4 = inf_divide(1997, 0)

# result
print(result1)
print(result2)
print(result3)
print(result4)
