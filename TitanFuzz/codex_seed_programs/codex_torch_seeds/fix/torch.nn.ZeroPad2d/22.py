'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
input_data = input_data.view(1, 1, 3, 4)
print('Input data: \n', input_data)
padding = (1, 1, 2, 2)
zero_pad = nn.ZeroPad2d(padding)
output = zero_pad(input_data)
print('Output data: \n', output)