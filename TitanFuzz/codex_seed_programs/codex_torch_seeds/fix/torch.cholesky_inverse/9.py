'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
input = torch.randn(2, 2)
print('Input: \n', input)
result = torch.cholesky_inverse(input)
print('Result: \n', result)