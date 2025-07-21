'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 3, 10)
avg_pool1d = nn.AdaptiveAvgPool1d(output_size=3)
output = avg_pool1d(input_data)
print('input_data: ', input_data)
print('output: ', output)