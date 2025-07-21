'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 10)
print('Input data: ', input_data)
output = nn.AdaptiveMaxPool1d(2)(input_data)
print('Output: ', output)