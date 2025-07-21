'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 3, 4)
gelu = nn.GELU()
output_data = gelu(input_data)
print('input_data:\n', input_data)
print('output_data:\n', output_data)