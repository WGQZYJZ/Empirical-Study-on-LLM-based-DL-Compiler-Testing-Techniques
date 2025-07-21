'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.narrow\ntorch.narrow(input, dim, start, length)\n'
import torch
x = torch.arange(1, 10, dtype=torch.float32).reshape(3, 3)
print('x:', x)
y = torch.narrow(x, dim=0, start=0, length=2)
print('y:', y)
y = torch.narrow(x, dim=0, start=1, length=2)
print('y:', y)
y = torch.narrow(x, dim=1, start=0, length=2)
print('y:', y)
y = torch.narrow(x, dim=1, start=1, length=2)
print('y:', y)