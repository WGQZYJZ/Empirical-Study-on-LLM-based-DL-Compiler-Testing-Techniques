'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky\ntorch.cholesky(input, upper=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
input = input.mm(input.t())
print(input)
result = torch.cholesky(input)
print(result)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_solve\ntorch.cholesky_solve(input, input2, upper=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
input = input.mm(input.t())
print(input)
input2 = torch.randn(3, 3)
print(input2)
result = torch.cholesky_solve(input, input2)
print(result)