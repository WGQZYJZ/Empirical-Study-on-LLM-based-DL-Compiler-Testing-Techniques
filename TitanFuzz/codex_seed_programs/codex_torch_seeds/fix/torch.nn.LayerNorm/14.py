'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
input_data = torch.randn(2, 3, 5)
print('Input data: ', input_data)
print('\nTask 3: Call the API torch.nn.LayerNorm')
layer_norm = nn.LayerNorm(input_data.size()[1:])
output = layer_norm(input_data)
print('Output data: ', output)