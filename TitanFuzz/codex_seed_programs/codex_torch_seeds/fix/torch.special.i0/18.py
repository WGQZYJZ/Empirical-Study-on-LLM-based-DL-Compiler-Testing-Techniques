'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0\ntorch.special.i0(input, *, out=None)\n'
import torch
input = torch.randn(10)
output = torch.special.i0(input)
print(output)
output = torch.special.i0(input, out=input)
print(output)