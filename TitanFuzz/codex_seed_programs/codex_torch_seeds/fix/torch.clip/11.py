'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clip\ntorch.clip(input, min=None, max=None, *, out=None)\n'
import torch
x = torch.randn(10)
print(x)
y = torch.clip(x, 0, 1)
print(y)
y = torch.clip(x, (- 1), 1)
print(y)
y = torch.clip(x, 0.5, 1)
print(y)
y = torch.clip(x, 0, 0.5)
print(y)