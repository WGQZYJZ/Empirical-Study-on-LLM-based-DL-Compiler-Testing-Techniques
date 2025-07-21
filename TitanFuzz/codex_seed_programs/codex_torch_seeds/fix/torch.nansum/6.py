'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nansum\ntorch.nansum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(3, 4)
print(input)
result = torch.nansum(input, dim=1, keepdim=True)
print(result)