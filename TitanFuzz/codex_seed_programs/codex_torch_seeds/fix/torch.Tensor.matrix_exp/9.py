'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_exp\ntorch.Tensor.matrix_exp(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.rand(3, 3)
output_tensor = torch.Tensor.matrix_exp(input_tensor)
print('Input Tensor:')
print(input_tensor)
print('Output Tensor:')
print(output_tensor)