'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arange\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
data = torch.arange(1, 4)
print(data)
data = torch.arange(1, 4, step=2)
print(data)
data = torch.arange(1, 4, step=2, dtype=torch.float32)
print(data)