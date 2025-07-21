'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool1d\ntorch.nn.functional.adaptive_avg_pool1d(input, output_size)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 5)
print('Input:', input_data)
output_size = 3
output = nn.functional.adaptive_avg_pool1d(input_data, output_size)
print('Output:', output)