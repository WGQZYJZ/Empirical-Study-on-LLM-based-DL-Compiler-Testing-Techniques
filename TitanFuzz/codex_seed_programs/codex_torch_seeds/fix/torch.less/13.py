'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.less\ntorch.less(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 3)
other = torch.randn(2, 3)
print(torch.less(input, other))