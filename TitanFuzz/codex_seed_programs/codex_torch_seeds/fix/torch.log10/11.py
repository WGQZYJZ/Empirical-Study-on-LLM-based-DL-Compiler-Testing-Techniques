'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
data = torch.randn(1)
print('Input data: ', data)
print('Output data: ', torch.log10(data))