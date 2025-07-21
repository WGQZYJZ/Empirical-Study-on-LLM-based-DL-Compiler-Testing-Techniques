'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eye\ntorch.eye(n, m=None, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
a = torch.rand(3, 3)
print(a)
print(torch.eye(3, 3))
print(torch.eye(3, 3, dtype=torch.int32))
print(torch.eye(3, 3, dtype=torch.float32))
print(torch.eye(3, 3, dtype=torch.float64))