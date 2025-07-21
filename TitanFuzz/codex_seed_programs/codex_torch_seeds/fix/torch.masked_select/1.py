'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.masked_select\ntorch.masked_select(input, mask, *, out=None)\n'
import torch
a = torch.randn(2, 3)
print(a)
print(a.shape)
b = torch.masked_select(a, (a > 0))
print(b)
print(b.shape)