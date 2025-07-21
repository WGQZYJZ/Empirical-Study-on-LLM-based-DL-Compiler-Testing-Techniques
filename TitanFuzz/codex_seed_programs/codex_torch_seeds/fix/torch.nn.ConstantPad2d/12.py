'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
input = torch.randn(3, 3, 3)
padding = (1, 1, 1, 1)
value = 0
pad = torch.nn.ConstantPad2d(padding, value)
output = pad(input)
print(output)