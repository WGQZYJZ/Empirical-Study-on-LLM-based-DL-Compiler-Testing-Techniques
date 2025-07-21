'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.subtract\ntorch.subtract(input, other, *, alpha=1, out=None)\n'
import torch
input = torch.randn(3, requires_grad=True)
other = torch.randn(3, requires_grad=True)
res = torch.subtract(input, other)
print(res)
print(input)
print(other)