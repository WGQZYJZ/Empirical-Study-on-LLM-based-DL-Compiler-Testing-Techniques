'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfinv\ntorch.special.erfinv(input, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print(input)
output = torch.special.erfinv(input)
print(output)