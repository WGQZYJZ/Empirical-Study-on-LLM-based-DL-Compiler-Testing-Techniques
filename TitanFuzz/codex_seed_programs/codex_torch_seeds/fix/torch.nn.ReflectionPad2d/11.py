'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad2d\ntorch.nn.ReflectionPad2d(padding)\n'
import torch
from torch.nn import ReflectionPad2d
input = torch.randn(1, 1, 3, 3)
padding = (1, 1, 1, 1)
output = ReflectionPad2d(padding)(input)
print(output)