'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfinv\ntorch.special.erfinv(input, *, out=None)\n'
import torch
input = torch.rand(1, dtype=torch.float64)
output = torch.special.erfinv(input)
print(output)