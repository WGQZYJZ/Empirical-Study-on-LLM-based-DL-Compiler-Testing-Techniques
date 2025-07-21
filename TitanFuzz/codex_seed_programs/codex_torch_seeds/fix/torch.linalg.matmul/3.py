'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(3, 4)
z = torch.linalg.matmul(x, y)
print(z)