'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_power\ntorch.matrix_power(input, n, *, out=None)\n'
import torch
x = torch.arange(1, 10, dtype=torch.float32).view(3, 3)
print('x:', x)
y = torch.matrix_power(x, 3)
print('y:', y)