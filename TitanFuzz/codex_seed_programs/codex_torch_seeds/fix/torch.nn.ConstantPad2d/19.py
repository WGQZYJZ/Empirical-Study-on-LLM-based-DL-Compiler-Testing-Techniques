'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
import numpy as np
import torch
input_data = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
output = torch.nn.ConstantPad2d((1, 2, 3, 4), 0)(input_data)
print('Input:')
print(input_data)
print('Output:')
print(output)