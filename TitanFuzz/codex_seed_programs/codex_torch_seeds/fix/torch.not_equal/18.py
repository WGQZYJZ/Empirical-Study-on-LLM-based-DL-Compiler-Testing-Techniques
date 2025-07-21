'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.not_equal\ntorch.not_equal(input, other, *, out=None)\n'
import torch
a = torch.randn(4, 4)
print(a)
b = torch.randn(4, 4)
print(b)
torch.not_equal(a, b)
torch.not_equal(a, b).sum()