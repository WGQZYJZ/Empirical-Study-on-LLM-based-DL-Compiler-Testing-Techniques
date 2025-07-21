'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
x = torch.arange(12).view(3, 2, 2)
print('x = ', x)
flatten = torch.nn.Flatten()
y = flatten(x)
print('y = ', y)
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
y = flatten(x)
print('y = ', y)