'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.msort\ntorch.msort(input, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print('Input data: ', input)
output = torch.msort(input)
print('Output data: ', output)