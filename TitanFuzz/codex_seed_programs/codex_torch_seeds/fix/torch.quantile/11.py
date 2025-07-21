'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4, 5)
q = torch.tensor([0.25, 0.5, 0.75])
torch.quantile(input, q, dim=None, keepdim=False, out=None)