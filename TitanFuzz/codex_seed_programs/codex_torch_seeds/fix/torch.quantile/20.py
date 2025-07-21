'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4)
input
torch.quantile(input, 0.5, dim=1)
torch.quantile(input, 0.5, dim=1, keepdim=True)
torch.quantile(input, 0.5, dim=1, keepdim=True, out=torch.randn(3, 1))
torch.quantile(input, torch.tensor([0.5, 0.9]), dim=1)
torch.quantile(input, torch.tensor([0.5, 0.9]), dim=1, keepdim=True)