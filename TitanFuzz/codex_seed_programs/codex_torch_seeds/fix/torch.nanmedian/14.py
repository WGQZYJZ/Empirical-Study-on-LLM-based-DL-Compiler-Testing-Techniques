'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
torch.nanmedian(input, dim=1)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nansum\ntorch.nansum(input, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
torch.nansum(input, dim=1)