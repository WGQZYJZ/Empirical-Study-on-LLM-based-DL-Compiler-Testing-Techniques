'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor\ntorch.Tensor.bitwise_xor(_input_tensor, other)\n'
import torch
import numpy as np
input_tensor = torch.Tensor(np.array([[1, 0, 0, 1], [0, 1, 1, 0]]))
other = torch.Tensor(np.array([[1, 0, 1, 0], [0, 1, 0, 1]]))
output_tensor = torch.Tensor.bitwise_xor(input_tensor, other)
print('Input tensor: ', input_tensor)
print('Other tensor: ', other)
print('Output tensor: ', output_tensor)