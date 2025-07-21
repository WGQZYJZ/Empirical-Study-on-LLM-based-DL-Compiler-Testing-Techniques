'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 3)
other = torch.randn(3, 3)
torch.less(input, other, out=None)
print(input)
print(other)
print(torch.less(input, other, out=None))