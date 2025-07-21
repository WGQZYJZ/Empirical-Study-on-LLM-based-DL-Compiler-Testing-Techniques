'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
x = torch.randn(1, 4)
print(x)
(sorted, indices) = torch.sort(x, dim=1)
print(sorted, indices)
(sorted, indices) = torch.sort(x, dim=0)
print(sorted, indices)
(sorted, indices) = torch.sort(x, dim=1, descending=True)
print(sorted, indices)