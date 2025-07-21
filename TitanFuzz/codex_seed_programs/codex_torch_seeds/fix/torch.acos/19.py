'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acos\ntorch.acos(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('The input data is: ', x)
out = torch.acos(x)
print('The output data is: ', out)