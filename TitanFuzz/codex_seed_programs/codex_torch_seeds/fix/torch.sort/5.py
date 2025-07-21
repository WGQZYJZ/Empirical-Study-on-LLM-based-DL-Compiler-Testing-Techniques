'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 5)
print(input)
print(torch.sort(input, dim=(- 1), descending=False, stable=False))
print(torch.sort(input, dim=(- 1), descending=True, stable=False))