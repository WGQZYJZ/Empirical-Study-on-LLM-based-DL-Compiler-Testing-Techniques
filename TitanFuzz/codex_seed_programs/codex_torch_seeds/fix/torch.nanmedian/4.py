'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
from torch import nn
input = torch.tensor([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]])
print(input)
print(torch.nanmedian(input, dim=(- 1), keepdim=False))