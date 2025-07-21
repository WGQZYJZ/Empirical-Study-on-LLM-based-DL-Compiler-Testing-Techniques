'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.max(input, dim=0)
torch.max(input, dim=1)
torch.max(input, dim=0, keepdim=True)
torch.max(input, dim=1, keepdim=True)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])