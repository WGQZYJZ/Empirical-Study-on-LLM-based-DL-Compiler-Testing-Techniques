'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach_\ntorch.Tensor.detach_(_input_tensor, )\n'
import torch
import numpy as np
input_tensor = torch.randn(10, 10)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.detach_(input_tensor)
print('Output tensor: ', output_tensor)