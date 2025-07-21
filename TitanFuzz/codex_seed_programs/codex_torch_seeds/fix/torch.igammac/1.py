'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igammac\ntorch.igammac(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3, dtype=torch.float64)
other = torch.randn(2, 3, dtype=torch.float64)
output = torch.igammac(input, other)
print(output)