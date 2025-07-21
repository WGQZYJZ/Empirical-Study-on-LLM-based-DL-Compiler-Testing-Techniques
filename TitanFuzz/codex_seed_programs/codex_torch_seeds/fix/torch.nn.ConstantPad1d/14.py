'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch.nn import ConstantPad1d
input_data = torch.arange(0, 12).reshape(1, 1, 12)
print('Input data: ', input_data)
padding = ConstantPad1d((2, 2), 0)
output = padding(input_data)
print('Output data: ', output)