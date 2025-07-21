'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diff\ntorch.diff(input, n=1, dim=-1, prepend=None, append=None)\n'
import torch
input = torch.randn(10, 20)
torch.diff(input, n=1, dim=(- 1), prepend=None, append=None)