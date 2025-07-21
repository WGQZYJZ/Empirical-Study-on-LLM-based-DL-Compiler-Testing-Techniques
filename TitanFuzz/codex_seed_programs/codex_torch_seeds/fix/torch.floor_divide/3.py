'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 5)
other = torch.randn(5)
torch.floor_divide(input, other, out=None)