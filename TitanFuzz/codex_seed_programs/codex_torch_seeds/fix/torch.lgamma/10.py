'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
input = torch.rand(1, dtype=torch.float)
output = torch.lgamma(input)
print(output)