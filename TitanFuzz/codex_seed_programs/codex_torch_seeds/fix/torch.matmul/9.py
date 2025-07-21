'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(3, 4)
z = torch.matmul(x, y)
print(z)