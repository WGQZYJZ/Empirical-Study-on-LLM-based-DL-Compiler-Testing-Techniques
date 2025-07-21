'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
q = torch.tensor([0.2, 0.5, 0.9])
torch.quantile(input, q, dim=0)
torch.quantile(input, q, dim=0, keepdim=True)
torch.quantile(input, q, dim=1)
torch.quantile(input, q, dim=1, keepdim=True)