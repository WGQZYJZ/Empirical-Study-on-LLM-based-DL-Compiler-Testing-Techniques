'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
input = torch.tensor([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]])
print('Input data: ', input)
print('Input data shape: ', input.shape)
pad = torch.nn.ConstantPad1d((2, 3), 0)
output = pad(input)
print('Output data: ', output)
print('Output data shape: ', output.shape)
input = torch.tensor([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]])
print('Input data: ', input)
print('Input data shape: ', input.shape)
pad = torch.nn.ConstantPad2d((1, 2, 3, 4), 0)
output = pad(input)
print('Output data: ', output)
print('Output data shape: ', output.shape)