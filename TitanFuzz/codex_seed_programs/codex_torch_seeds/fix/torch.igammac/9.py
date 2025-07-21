'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.igammac\ntorch.igammac(input, other, *, out=None)\n'
import torch
input = torch.randn(1, 2, 3, dtype=torch.float, requires_grad=True)
other = torch.randn(1, 2, 3, dtype=torch.float, requires_grad=True)
print(torch.igammac(input, other))