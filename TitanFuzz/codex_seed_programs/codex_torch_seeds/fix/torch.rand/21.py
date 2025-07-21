'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.rand(3, 3)
print(x)
y = torch.rand(2, 2)
print(y)
z = torch.rand(3, 3)
print(z)
w = torch.rand(3, 3)
print(w)