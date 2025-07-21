'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmin\ntorch.nn.Softmin(dim=None)\n'
import torch
import torch
x = torch.randn(2, 3)
print('Input data:')
print(x)
y = torch.nn.Softmin(dim=1)(x)
print('Output data:')
print(y)