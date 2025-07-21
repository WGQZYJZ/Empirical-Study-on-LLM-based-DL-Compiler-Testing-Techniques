'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 2)
selu = nn.SELU(inplace=False)
output = selu(input_data)
print('input_data:', input_data)
print('output:', output)