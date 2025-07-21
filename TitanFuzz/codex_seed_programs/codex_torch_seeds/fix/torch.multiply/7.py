'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multiply\ntorch.multiply(input, other, *, out=None)\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
z = torch.multiply(x, y)
print(z)