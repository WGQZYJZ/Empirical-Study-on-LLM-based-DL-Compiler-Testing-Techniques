'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_solve\ntorch.cholesky_solve(input, input2, upper=False, *, out=None)\n'
import torch
A = torch.rand(3, 3)
b = torch.rand(3, 1)
x = torch.cholesky_solve(b, A)
print(x)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
A = torch.rand(3, 3)
x = torch.cholesky_inverse(A)
print(x)