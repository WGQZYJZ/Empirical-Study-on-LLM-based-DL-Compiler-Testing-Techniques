'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(1, 1, 4, 4)
pooling_layer = nn.AdaptiveMaxPool2d(output_size=2)
output_data = pooling_layer(input_data)
print('Input data: \n', input_data)
print('Output data: \n', output_data)