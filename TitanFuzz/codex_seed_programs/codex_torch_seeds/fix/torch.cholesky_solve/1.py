'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_solve\ntorch.cholesky_solve(input, input2, upper=False, *, out=None)\n'
import torch
A = torch.randn(3, 3)
b = torch.randn(3, 1)
x = torch.cholesky_solve(b, A)
print(x)
print(torch.mm(A, x))
print(b)