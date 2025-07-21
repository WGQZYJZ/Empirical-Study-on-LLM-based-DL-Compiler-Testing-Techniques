'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(1, 3)
torch.max(input, dim=0, keepdim=False, out=None)