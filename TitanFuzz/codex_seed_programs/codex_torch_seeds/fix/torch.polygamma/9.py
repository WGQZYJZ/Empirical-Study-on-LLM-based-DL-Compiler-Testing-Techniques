'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
input = torch.randn(4, 4, dtype=torch.float)
output = torch.polygamma(1, input)
print(output)