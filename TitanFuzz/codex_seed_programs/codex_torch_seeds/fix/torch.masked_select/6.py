'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
import torch
x = torch.randn(2, 3)
print('x = ', x)
y = torch.masked_select(x, (x > 0))
print('y = ', y)