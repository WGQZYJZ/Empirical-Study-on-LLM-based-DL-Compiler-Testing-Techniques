'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.histc\ntorch.histc(input, bins=100, min=0, max=0, *, out=None)\n'
import torch
import torch
input = (torch.rand(100, 1) * 100)
torch.histc(input, bins=100, min=0, max=0, out=None)