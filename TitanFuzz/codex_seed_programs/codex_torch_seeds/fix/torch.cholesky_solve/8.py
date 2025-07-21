'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_solve\ntorch.cholesky_solve(input, input2, upper=False, *, out=None)\n'
import torch
import torch
a = torch.rand(3, 3)
b = torch.rand(3, 1)
x = torch.cholesky_solve(b, a)
print(x)
print(torch.mm(a, x))
print(b)
x = torch.cholesky_solve(b, a)
print(x)
print(torch.mm(a, x))
print(b)
x = torch.cholesky_solve(b, a)
print(x)
print(torch.mm(a, x))
print(b)