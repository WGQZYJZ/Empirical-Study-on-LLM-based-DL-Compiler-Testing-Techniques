'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
x = torch.randn(3, 3)
print('x: ', x)
print('torch.diag(x): ', torch.diag(x))
print('torch.diag(x, diagonal=1): ', torch.diag(x, diagonal=1))
print('torch.diag(x, diagonal=-1): ', torch.diag(x, diagonal=(- 1)))