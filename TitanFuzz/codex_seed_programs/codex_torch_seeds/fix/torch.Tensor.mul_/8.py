'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(_input_tensor, value)\n'
import torch
import numpy as np
input_tensor = torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]]))
print('Input tensor:')
print(input_tensor)
scalar = 2
output_tensor = torch.Tensor.mul_(input_tensor, scalar)
print('Output tensor:')
print(output_tensor)