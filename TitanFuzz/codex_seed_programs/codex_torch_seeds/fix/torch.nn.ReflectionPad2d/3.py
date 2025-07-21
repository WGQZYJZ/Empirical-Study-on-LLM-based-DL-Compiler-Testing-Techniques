'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad2d\ntorch.nn.ReflectionPad2d(padding)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 3, 3)
padding = 1
reflection_pad = nn.ReflectionPad2d(padding)
output = reflection_pad(input)
print(output)