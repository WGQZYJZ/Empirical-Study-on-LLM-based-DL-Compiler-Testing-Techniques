'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
y = torch.reciprocal(x)
print('x:', x)
print('y:', y)