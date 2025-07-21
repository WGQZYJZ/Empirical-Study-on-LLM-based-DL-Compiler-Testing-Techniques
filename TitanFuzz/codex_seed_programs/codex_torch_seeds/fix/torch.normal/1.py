'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.normal\ntorch.normal(mean, std, size, *, out=None)\n'
import torch
mean = torch.tensor(0.0)
std = torch.tensor(1.0)
size = torch.Size([3, 3])
torch.normal(mean, std, size)
torch.normal(mean, std, size, out=None)