'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccosh\ntorch.Tensor.arccosh(_input_tensor)\n'
import torch
import numpy as np
import torch
input_tensor = torch.Tensor(np.random.random((1, 2, 3)))
print('Input tensor:', input_tensor)
output_tensor = torch.Tensor.arccosh(input_tensor)
print('Output tensor:', output_tensor)