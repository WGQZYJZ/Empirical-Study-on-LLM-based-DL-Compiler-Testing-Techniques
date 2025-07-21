'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
x = torch.rand(5, 5)
y = torch.rand(5, 5)
z = torch.rand(5, 5)
print(torch.greater(x, y))
print(torch.greater(x, y, out=z))
print(z)