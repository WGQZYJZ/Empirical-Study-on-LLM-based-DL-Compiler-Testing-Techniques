'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.range\ntorch.range(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.range(start=0, end=10, step=1)
print(x)
print(y)