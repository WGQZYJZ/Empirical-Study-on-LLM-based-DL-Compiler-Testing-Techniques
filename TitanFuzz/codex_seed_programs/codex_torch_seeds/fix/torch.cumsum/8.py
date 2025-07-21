'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
input = torch.arange(0, 4, 1, dtype=torch.float32)
print(input)
output = torch.cumsum(input, dim=0)
print(output)