'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
torch.quantile(input, 0.5)
torch.quantile(input, 0.5, dim=0)
torch.quantile(input, 0.5, dim=1)
torch.quantile(input, 0.5, dim=1, keepdim=True)