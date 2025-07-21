'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
import torch
input = torch.randn(2, 3, 4)
torch.mean(input, dim=1)