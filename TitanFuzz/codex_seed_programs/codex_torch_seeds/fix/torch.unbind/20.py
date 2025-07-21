'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unbind\ntorch.unbind(input, dim=0)\n'
import torch
x = torch.randn(2, 3)
print('Input: ', x)
y = torch.unbind(x, dim=0)
print('Output: ', y)