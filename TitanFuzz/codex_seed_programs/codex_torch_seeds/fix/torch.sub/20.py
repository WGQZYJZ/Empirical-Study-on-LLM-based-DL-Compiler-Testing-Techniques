'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.sub(a, b)
print(c)
'\nTask 4: Call the API torch.sub_\ntorch.sub_(input, other, *, alpha=1)\n'
a = torch.randn(4, 4)
b = torch.randn(4, 4)
a.sub_(b)
print(a)
'\nTask 5: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.mul(a, b)
print(c)
'\nTask 6: Call the API torch.mul_\ntorch.mul_(input, other, *, alpha=1)\n'
a = torch.randn(4, 4)
b = torch.randn(4, 4)
a.mul_(b)