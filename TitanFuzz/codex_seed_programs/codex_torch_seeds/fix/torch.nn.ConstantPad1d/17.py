'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
data = torch.arange(6, dtype=torch.float).reshape(1, 1, 6)
print('Input data:\n', data)
padding = 2
value = 0
result = torch.nn.ConstantPad1d(padding, value)(data)
print('Result:\n', result)