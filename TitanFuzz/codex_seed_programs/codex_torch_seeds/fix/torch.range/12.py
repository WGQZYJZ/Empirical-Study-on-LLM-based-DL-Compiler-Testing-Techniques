'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.range\ntorch.range(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.range(1, 10)
print(x)
y = torch.range(1, 10, 2)
print(y)
z = torch.range(1, 10, 0.5)
print(z)