'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atan\ntorch.atan(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1.0), 0.0, 1.0])
print('x:', x)
y = torch.atan(x)
print('y:', y)
y = torch.atan_(x)
print('y:', y)
print('x:', x)