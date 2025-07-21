'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
input = torch.randn(1, 3, 3, 3)
pad = torch.nn.ConstantPad2d((1, 1, 1, 1), 0)
output = pad(input)
print(output)