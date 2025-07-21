'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
import torch
x = torch.rand(3, 3, dtype=torch.float)
print('x:', x)
y = torch.reciprocal(x)
print('y:', y)