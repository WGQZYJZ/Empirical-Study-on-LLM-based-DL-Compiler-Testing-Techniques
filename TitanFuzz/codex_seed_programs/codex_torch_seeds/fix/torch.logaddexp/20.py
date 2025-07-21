'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logaddexp\ntorch.logaddexp(input, other, *, out=None)\n'
import torch
input = torch.randn(4)
other = torch.randn(4)
print(torch.logaddexp(input, other))
input = torch.randn(4, 1)
other = torch.randn(1, 4)
print(torch.logaddexp(input, other))