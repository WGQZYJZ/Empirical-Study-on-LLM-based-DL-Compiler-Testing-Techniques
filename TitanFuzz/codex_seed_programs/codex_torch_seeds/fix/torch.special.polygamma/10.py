'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
input = torch.randn(1, dtype=torch.float)
output = torch.special.polygamma(1, input)
print(output)