'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 2, 3)
print('Input data: ', input_data)
gelu = nn.GELU()
output_data = gelu(input_data)
print('Output data: ', output_data)