'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atan_\ntorch.Tensor.atan_(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(1, 3, 3)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.atan_()
print('Output tensor: ', output_tensor)