'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.i0\ntorch.i0(input, *, out=None)\n'
import torch
input = torch.randn(1, dtype=torch.float)
output = torch.i0(input)
print(output)