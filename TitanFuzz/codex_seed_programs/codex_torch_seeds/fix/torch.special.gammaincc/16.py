'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaincc\ntorch.special.gammaincc(input, other, *, out=None)\n'
import torch
input = torch.randn(3)
other = torch.randn(3)
out = torch.empty(3)
torch.special.gammaincc(input, other, out=out)
print(out)
torch.special.gammaincc(input, other)