'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
import torch
input = torch.randn(10, 10)
print('input: \n', input)
print('signbit: \n', torch.signbit(input))