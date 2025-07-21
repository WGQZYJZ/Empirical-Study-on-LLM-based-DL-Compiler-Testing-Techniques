'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
torch.all(input, dim=0)
torch.all(input, dim=1)