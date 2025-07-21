'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
input = torch.randn(1, 2, 3, dtype=torch.float, requires_grad=True)
result = torch.lgamma(input)
print(result)