'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
x = torch.randn(2, 3, 3)
print('Input data: ', x)
padding = (0, 1)
value = 1
y = torch.nn.ConstantPad1d(padding, value)(x)
print('Output data: ', y)