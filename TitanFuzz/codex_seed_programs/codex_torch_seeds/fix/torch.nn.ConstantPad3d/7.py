'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
data = torch.randn(1, 1, 3, 3, 3)
print('Input data: ', data)
padding = (1, 1, 1, 1, 1, 1)
value = 0
result = torch.nn.ConstantPad3d(padding, value)(data)
print('Result: ', result)