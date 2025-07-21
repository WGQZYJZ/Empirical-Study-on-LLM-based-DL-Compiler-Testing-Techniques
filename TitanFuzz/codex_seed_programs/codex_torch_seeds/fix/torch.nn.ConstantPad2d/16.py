'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
input = torch.randn(1, 3, 3, 3)
padding = (1, 1, 1, 1)
value = 0
output = torch.nn.ConstantPad2d(padding, value)(input)
print('Input:')
print(input)
print('Output:')
print(output)