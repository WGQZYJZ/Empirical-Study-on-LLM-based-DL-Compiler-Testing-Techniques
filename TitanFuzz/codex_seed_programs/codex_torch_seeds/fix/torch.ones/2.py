'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ones\ntorch.ones(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.rand(3, 3)
print(x)
y = torch.ones(3, 3)
print(y)
z = torch.zeros(3, 3)
print(z)