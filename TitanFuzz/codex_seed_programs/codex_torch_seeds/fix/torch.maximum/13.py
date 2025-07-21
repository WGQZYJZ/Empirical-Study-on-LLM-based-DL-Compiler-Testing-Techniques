'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.maximum\ntorch.maximum(input, other, *, out=None)\n'
import torch
import torch
input = torch.rand(2, 3)
other = torch.rand(2, 3)
torch.maximum(input, other)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input)\ntorch.max(input, dim, keepdim=False, out=None)\ntorch.max(input, other, out=None)\n'
import torch
import torch
input = torch.rand(2, 3)
other = torch.rand(2, 3)
torch.max(input)
torch.max(input, dim=0, keepdim=False)
torch.max(input, other)