'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igammac\ntorch.igammac(input, other, *, out=None)\n'
import torch
input = torch.rand(1, 1, dtype=torch.float64)
other = torch.tensor([2.0], dtype=torch.float64)
print(torch.igammac(input, other))