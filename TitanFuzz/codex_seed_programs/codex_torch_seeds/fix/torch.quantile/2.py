'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
q = torch.tensor([0.1, 0.5, 0.9])
print(torch.quantile(input, q, dim=1))