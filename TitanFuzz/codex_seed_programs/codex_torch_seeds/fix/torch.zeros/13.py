'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
data = torch.zeros(2, 3)
print(data)