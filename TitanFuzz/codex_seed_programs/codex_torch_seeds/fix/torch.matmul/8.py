'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.matmul(a, b)
print(c)