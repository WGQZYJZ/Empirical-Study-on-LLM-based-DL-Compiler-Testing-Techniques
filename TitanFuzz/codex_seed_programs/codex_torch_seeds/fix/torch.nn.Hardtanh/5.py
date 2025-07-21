'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 3, 10, 10)
print('input_data:', input_data)
hardtanh = nn.Hardtanh(min_val=(- 1.0), max_val=1.0, inplace=False)
output = hardtanh(input_data)
print('output:', output)