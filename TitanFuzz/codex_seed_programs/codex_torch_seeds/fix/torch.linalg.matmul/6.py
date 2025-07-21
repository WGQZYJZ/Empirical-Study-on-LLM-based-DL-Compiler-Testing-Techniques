'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
a = torch.randn(3, 4)
b = torch.randn(4, 5)
c = torch.linalg.matmul(a, b)
print(c)