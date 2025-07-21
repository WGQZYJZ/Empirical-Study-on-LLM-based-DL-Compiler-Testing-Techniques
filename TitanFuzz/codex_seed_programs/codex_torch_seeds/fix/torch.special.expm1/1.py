'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.expm1\ntorch.special.expm1(input, *, out=None)\n'
import torch
input = torch.randn(1, dtype=torch.float)
print(input)
output = torch.special.expm1(input)
print(output)