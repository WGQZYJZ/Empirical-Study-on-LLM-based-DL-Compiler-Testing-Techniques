'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_solve\ntorch.cholesky_solve(input, input2, upper=False, *, out=None)\n'
import torch
a = torch.randn(3, 3)
a = torch.mm(a.t(), a)
b = torch.randn(3, 2)
x = torch.cholesky_solve(b, a)
print(x)
print(torch.matmul(a, x))