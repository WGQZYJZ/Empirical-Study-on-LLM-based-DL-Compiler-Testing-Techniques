'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.zeta\ntorch.special.zeta(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3)
other = torch.randn(2, 3)
import torch
input = torch.randn(2, 3)
other = torch.randn(2, 3)
torch.special.zeta(input, other, out=None)
print(torch.special.zeta(input, other, out=None))