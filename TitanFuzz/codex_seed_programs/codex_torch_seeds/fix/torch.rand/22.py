'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
size = (3, 3)
torch.rand(*size)
torch.rand(size=size)
torch.rand(size=size, dtype=torch.float32)
torch.rand(size=size, dtype=torch.float32, layout=torch.strided)