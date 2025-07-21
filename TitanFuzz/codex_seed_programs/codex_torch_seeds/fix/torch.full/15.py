'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
size = (2, 3)
fill_value = 2.0
out = torch.full(size, fill_value)
print(out)