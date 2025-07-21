'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.any\ntorch.any(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.tensor([[1, 1, 1, 1], [0, 0, 0, 0]])
torch.any(input, dim=0)
torch.any(input, dim=1)
torch.any(input, dim=1, keepdim=True)
torch.any(input, dim=(- 1), keepdim=True)
torch.any(input, dim=(- 1), keepdim=False)
torch.any(input, dim=0, keepdim=True)