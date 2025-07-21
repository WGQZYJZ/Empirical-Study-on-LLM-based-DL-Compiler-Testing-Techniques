'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapdims\ntorch.swapdims(input, dim0, dim1)\n'
import torch
x = torch.arange(6).view(2, 3)
print('x = ', x)
y = torch.swapdims(x, 0, 1)
print('y = ', y)