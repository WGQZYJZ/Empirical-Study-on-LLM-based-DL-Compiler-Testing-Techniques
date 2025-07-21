'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch.nn import ConstantPad1d
input_data = torch.arange(1, 5, dtype=torch.float).view(1, 1, 4)
padding = (1, 2)
value = (- 1)
cp1d = ConstantPad1d(padding, value)
output = cp1d(input_data)
print('Input data:', input_data)
print('Output data:', output)