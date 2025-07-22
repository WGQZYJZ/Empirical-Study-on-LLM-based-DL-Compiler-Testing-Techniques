import torch

x = torch.randn(2, 3)

def func(x):
    xz = x[:]
    x.data = torch.ones(3, 4)
    return xz

res1 = func(x)
jit_func = torch.compile(func)
print(res1)
res2 = jit_func(x)
print(res2)