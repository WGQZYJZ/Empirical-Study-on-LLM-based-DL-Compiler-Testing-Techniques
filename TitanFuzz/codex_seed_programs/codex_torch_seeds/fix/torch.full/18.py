'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.full((2,), 10.0)
print(x)
x = torch.randn(2, 3)
print(x)
x = torch.full((2, 3), 10.0)
print(x)