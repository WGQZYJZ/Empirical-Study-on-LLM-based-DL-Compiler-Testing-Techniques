'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mm\ntorch.mm(input, mat2, *, out=None)\n'
import torch
a = torch.randn(4, 3)
b = torch.randn(3, 5)
c = torch.mm(a, b)
print(c)