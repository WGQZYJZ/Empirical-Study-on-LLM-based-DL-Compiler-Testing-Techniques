'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
import torch
x = torch.randn(3, 4)
mask = x.ge(0.5)
print(x)
print(mask)
y = torch.masked_select(x, mask)
print(y)