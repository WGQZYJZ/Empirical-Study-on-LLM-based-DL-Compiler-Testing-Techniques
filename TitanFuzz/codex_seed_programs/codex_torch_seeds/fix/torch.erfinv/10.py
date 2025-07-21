'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfinv\ntorch.erfinv(input, *, out=None)\n'
import torch
x = torch.randn(4)
print('Input: ', x)
output = torch.erfinv(x)
print('Output: ', output)