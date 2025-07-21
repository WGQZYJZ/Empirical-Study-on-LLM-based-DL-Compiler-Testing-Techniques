'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.msort\ntorch.msort(input, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4, 5)
output = torch.msort(input)
print('output = ', output)