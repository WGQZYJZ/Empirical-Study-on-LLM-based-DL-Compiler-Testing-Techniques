'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
import numpy as np
gelu = torch.nn.GELU()
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
output = gelu(input_data)
print('input_data:', input_data)
print('output:', output)