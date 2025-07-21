'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.exp2\ntorch.special.exp2(input, *, out=None)\n'
import torch
input = torch.randn(1, 3, 3)
print(input)
print(torch.special.exp2(input))