'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
input = torch.randn(1, 3, 5)
print('input: ', input)
padding = (2, 3)
value = 0
output = torch.nn.ConstantPad1d(padding, value)(input)
print('output: ', output)