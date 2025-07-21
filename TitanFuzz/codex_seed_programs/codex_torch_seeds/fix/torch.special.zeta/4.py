'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.zeta\ntorch.special.zeta(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 3)
other = torch.randn(3, 3)
output = torch.special.zeta(input, other)
print(output)