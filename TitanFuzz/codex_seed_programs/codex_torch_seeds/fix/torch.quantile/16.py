'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantile\ntorch.quantile(input, q, dim=None, keepdim=False, *, out=None)\n'
import torch
data = torch.randn(5, 5)
print(data)
quantile_value = torch.quantile(data, 0.9)
print(quantile_value)