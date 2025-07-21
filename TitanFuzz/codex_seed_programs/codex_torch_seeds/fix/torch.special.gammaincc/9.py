'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaincc\ntorch.special.gammaincc(input, other, *, out=None)\n'
import torch
x = torch.randn(2, 3)
other = torch.randn(2, 3)
print(torch.special.gammaincc(x, other))