'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bmm\ntorch.bmm(input, mat2, *, deterministic=False, out=None)\n'
import torch
a = torch.randn(2, 3, 4)
b = torch.randn(2, 4, 5)
c = torch.bmm(a, b)
print(c)