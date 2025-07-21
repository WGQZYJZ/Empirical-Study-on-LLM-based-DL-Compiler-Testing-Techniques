'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
input = torch.randn(4, 3)
other = torch.randn(4, 3)
torch.hypot(input, other)