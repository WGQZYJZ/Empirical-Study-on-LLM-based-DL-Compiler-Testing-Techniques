'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asinh\ntorch.asinh(input, *, out=None)\n'
import torch
input = torch.randn(1, 3, 4, 5)
print(input)
print(torch.asinh(input))