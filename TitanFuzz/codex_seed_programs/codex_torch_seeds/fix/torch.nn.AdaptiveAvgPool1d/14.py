'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
import numpy as np
import torch.nn as nn
input_data = torch.tensor([[[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]]], dtype=torch.float32)
pool = nn.AdaptiveAvgPool1d(output_size=3)
output = pool(input_data)
print('input_data:\n', input_data)
print('output:\n', output)