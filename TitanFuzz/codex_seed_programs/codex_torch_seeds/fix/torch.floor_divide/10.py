'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3, dtype=torch.float)
other = torch.randn(2, 3, dtype=torch.float)
torch.floor_divide(input, other)
torch.floor_divide(input, other, out=None)
torch.floor_divide(input, other, out=torch.empty(2, 3))