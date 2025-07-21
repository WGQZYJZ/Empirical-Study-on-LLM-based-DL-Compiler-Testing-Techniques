'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
import numpy as np
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.narrow(input_tensor, 1, 1, 2)
print('Input Tensor:')
print(input_tensor)
print('Output Tensor:')
print(output_tensor)