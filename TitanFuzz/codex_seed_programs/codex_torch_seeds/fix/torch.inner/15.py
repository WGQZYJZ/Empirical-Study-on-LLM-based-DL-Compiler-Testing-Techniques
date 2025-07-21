'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inner\ntorch.inner(input, other, *, out=None)\n'
import torch
input = torch.randn(4, 10)
other = torch.randn(10)
output = torch.inner(input, other)
print(output)