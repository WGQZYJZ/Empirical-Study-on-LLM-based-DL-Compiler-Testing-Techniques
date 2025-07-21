'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
a = torch.randn(2, 3, requires_grad=True)
b = torch.randn(3, 4, requires_grad=True)
c = torch.linalg.matmul(a, b)
print(c)