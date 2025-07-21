'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad2d\ntorch.nn.ReflectionPad2d(padding)\n'
import torch
from torch.nn import ReflectionPad2d
input_data = torch.arange(1, 9, dtype=torch.float).view(1, 1, 2, 4)
print('Input data:\n', input_data)
pad = ReflectionPad2d(padding=1)
output = pad(input_data)
print('Output data:\n', output)
print('Output shape:', output.shape)