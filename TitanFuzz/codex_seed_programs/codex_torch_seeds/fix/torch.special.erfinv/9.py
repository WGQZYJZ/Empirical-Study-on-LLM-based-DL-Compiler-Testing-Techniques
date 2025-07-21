'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfinv\ntorch.special.erfinv(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print(input)
result = torch.special.erfinv(input)
print(result)