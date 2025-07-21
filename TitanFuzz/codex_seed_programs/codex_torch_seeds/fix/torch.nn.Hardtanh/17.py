'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
import numpy as np
input_data = torch.randn(1, 3, 3)
print(input_data)
output_data = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)(input_data)
print(output_data)