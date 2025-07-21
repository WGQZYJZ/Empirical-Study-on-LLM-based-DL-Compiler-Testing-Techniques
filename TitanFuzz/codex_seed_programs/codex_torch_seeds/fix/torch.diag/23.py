'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('input = ', input)
output = torch.diag(input)
print('output = ', output)
output = torch.diag(input, diagonal=1)
print('output = ', output)
output = torch.diag(input, diagonal=(- 1))
print('output = ', output)