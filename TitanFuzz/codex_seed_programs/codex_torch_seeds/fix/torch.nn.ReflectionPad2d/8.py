'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad2d\ntorch.nn.ReflectionPad2d(padding)\n'
import torch
input = torch.ones(1, 1, 3, 3)
print('Input data: ', input)
pad = torch.nn.ReflectionPad2d(1)
output = pad(input)
print('Output data: ', output)