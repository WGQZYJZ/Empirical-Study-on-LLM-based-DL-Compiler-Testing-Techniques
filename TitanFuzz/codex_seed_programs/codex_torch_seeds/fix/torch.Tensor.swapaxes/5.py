'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
import numpy as np
input_tensor = torch.Tensor(np.arange(24).reshape(2, 3, 4))
print('Input tensor: ')
print(input_tensor)
output_tensor = input_tensor.swapaxes(0, 2)
print('Output tensor: ')
print(output_tensor)