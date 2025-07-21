'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.zeta\ntorch.special.zeta(input, other, *, out=None)\n'
import torch
input = torch.randn(1, requires_grad=True)
other = torch.randn(1, requires_grad=True)
output = torch.special.zeta(input, other)
print(output)