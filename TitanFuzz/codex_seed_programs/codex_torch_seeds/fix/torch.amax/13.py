'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(5, 5)
torch.amax(input)
torch.amax(input, dim=0)
torch.amax(input, dim=0, keepdim=True)
torch.amax(input, dim=(- 1))
torch.amax(input, dim=(- 1), keepdim=True)