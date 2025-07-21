'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad2d\ntorch.nn.ReflectionPad2d(padding)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 3, 5, 5)
pad = nn.ReflectionPad2d(2)
output = pad(input)
print(output)