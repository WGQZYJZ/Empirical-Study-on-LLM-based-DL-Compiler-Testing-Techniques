'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
from torch.nn import ConstantPad3d
input_data = torch.randn(2, 3, 3, 3, 3)
pad_layer = ConstantPad3d((1, 1, 1, 1, 1, 1), 2)
output = pad_layer(input_data)
print('Input shape: ', input_data.shape)
print('Output shape: ', output.shape)
print('Output data: ', output)