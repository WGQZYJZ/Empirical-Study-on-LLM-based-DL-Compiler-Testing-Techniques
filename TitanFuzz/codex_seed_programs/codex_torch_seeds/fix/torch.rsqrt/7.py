'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
import torch
import torch
a = torch.randn(4)
print('Input: ', a)
output = torch.rsqrt(a)
print('Output: ', output)