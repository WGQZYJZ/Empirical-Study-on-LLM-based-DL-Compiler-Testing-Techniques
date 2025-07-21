'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flipud\ntorch.flipud(input)\n'
import torch
x = torch.rand(3, 3)
print('Input: \n', x)
y = torch.flipud(x)
print('Output: \n', y)