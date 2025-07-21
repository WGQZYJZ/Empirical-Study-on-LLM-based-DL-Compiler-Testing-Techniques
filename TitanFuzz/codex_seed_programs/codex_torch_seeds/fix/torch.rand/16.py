'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.rand(2, 3)
print(x)
y = torch.rand(2, 3, dtype=torch.float64)
print(y)
z = torch.rand(2, 3, layout=torch.strided, dtype=torch.float64, device=torch.device('cpu'), requires_grad=True)
print(z)