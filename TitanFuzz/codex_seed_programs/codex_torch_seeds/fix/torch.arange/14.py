'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arange\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
data = torch.arange(1, 3)
print(data)
data = torch.arange(1, 3, 0.5)
print(data)
data = torch.arange(1, 3, 0.5, dtype=torch.float32)
print(data)
data = torch.arange(1, 3, 0.5, dtype=torch.float32, device='cuda')
print(data)
data = torch.arange(1, 3, 0.5, dtype=torch.float32, device='cuda', requires_grad=True)
print(data)