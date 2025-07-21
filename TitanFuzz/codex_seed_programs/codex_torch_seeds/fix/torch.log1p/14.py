'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log1p\ntorch.log1p(input, *, out=None)\n'
import torch
import torch
x = torch.randn(3, 4)
print(x)
print(x.size())
y = torch.log1p(x)
print(y)
print(y.size())