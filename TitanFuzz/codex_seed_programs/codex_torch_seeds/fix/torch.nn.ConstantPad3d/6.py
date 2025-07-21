'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
input_data = torch.randn(2, 3, 4, 4, 4)
output_data = torch.nn.ConstantPad3d((0, 0, 0, 0, 1, 1), 0)(input_data)
print('Input data: \n', input_data)
print('Output data: \n', output_data)