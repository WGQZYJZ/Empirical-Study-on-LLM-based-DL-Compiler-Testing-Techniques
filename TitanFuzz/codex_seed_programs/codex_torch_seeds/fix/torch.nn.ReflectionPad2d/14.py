'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad2d\ntorch.nn.ReflectionPad2d(padding)\n'
import torch
input_data = torch.randn(1, 1, 3, 3)
print('Input data = ', input_data)
pad = torch.nn.ReflectionPad2d((1, 1, 1, 1))
output = pad(input_data)
print('Output = ', output)