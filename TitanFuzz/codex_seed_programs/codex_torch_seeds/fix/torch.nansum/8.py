'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nansum\ntorch.nansum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(2, 3, 4)
print(input)
output = torch.nansum(input, dim=2, keepdim=True)
print(output)