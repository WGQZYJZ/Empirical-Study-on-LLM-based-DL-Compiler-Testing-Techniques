'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matmul\ntorch.linalg.matmul(input, other, *, out=None)\n'
import torch
x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = torch.linalg.matmul(x, y)
print(z)