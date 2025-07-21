'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
import torch
import numpy as np
input_tensor = torch.rand(2, 3)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.transpose(0, 1)
print('output_tensor: ', output_tensor)
input_tensor_np = input_tensor.numpy()
output_tensor_np = np.transpose(input_tensor_np)
print('output_tensor_np: ', output_tensor_np)