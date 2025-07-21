'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 3)
print('input_data: ', input_data)
gelu_layer = nn.GELU()
output_data = gelu_layer(input_data)
print('output_data: ', output_data)