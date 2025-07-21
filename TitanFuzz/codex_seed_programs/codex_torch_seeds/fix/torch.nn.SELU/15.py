'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(5, 3)
print('Input data is: ', input_data)
selu = nn.SELU()
output = selu(input_data)
print('Output is: ', output)