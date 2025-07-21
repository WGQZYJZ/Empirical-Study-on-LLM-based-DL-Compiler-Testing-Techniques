'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cholesky_inverse\ntorch.cholesky_inverse(input, upper=False, *, out=None)\n'
import torch
input = torch.randn(2, 2)
print('Input:', input)
print('Input shape:', input.shape)
print('Input type:', input.dtype)
output = torch.cholesky_inverse(input)
print('Output:', output)
print('Output shape:', output.shape)
print('Output type:', output.dtype)