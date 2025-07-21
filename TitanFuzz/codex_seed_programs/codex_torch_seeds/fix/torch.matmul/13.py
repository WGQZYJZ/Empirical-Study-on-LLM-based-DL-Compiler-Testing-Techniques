'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
x = torch.randn(4, 3)
y = torch.randn(3, 5)
z = torch.matmul(x, y)
print(z)