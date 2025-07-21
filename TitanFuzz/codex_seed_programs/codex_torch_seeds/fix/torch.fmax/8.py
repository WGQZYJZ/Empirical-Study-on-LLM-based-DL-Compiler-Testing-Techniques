'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3)
other = torch.randn(2, 3)
torch.fmax(input, other)
out = torch.empty(2, 3)
torch.fmax(input, other, out=out)
print(out)