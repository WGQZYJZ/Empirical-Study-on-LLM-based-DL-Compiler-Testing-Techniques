'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
import torch
input_data = torch.randn(1, 1, 4, 4, 4)
pad = torch.nn.ConstantPad3d((1, 2, 3, 4, 5, 6), 0)
output = pad(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
import torch
input_data = torch.randn(1, 1, 4)
pad = torch.nn.ConstantPad1d((1, 2), 0)
output = pad(input_data)
print(output)