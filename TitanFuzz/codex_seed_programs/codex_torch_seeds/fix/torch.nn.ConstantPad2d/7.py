'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.tensor([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]])
print(input_data.shape)
pad = nn.ConstantPad2d(2, 3)
output = pad(input_data)
print(output)