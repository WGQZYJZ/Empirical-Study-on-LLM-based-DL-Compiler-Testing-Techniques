'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.minimum\ntorch.minimum(input, other, *, out=None)\n'
import torch
input = torch.randn(5, 5)
other = torch.randn(5, 5)
print(torch.minimum(input, other))