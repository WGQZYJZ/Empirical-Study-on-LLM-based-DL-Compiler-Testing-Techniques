'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
import numpy as np
input_tensor = torch.Tensor(np.arange(1, 13).reshape(3, 4))
print('Input tensor: \n', input_tensor)
split_size = 2
dim = 0
output_tensor_list = input_tensor.split(split_size, dim)
print('Output tensor list: \n', output_tensor_list)