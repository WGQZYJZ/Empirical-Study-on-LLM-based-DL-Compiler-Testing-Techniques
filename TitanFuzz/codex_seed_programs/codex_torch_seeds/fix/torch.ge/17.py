'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ge\ntorch.ge(input, other, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([1, 1, 1, 1])
print('x:', x)
print('y:', y)
print('torch.ge(x, y):', torch.ge(x, y))
print('torch.ge(y, x):', torch.ge(y, x))