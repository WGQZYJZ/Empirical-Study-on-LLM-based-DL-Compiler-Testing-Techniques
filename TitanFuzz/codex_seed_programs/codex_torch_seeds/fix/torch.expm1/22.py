'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.expm1\ntorch.expm1(input, *, out=None)\n'
import torch
data = torch.randn(2, 3)
print('Input: ', data)
print('Output: ', torch.expm1(data))