'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensordot\ntorch.tensordot(a, b, dims=2, out=None)\n'
import torch
a = torch.randn(3, 4)
b = torch.randn(4, 5)
c = torch.tensordot(a, b, dims=1)
print(c.size())