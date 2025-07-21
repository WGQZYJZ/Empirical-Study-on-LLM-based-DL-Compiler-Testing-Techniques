'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad2d\ntorch.nn.ReflectionPad2d(padding)\n'
import torch
import torch.nn as nn
input = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], dtype=torch.float32).reshape(1, 1, 4, 4)
print('Input: ', input)
reflection_pad = nn.ReflectionPad2d(2)
output = reflection_pad(input)
print('Output: ', output)