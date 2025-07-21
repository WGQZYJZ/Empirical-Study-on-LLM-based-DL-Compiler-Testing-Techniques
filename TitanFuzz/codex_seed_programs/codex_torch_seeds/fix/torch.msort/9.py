'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.msort\ntorch.msort(input, *, out=None)\n'
import torch
input = torch.randn(3, 2)
print('input:', input)
output = torch.msort(input)
print('output:', output)