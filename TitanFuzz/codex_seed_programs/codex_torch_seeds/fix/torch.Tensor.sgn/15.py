'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn\ntorch.Tensor.sgn(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(3, 4)
print('Input tensor: \n{}\n'.format(input_tensor))
output_tensor = torch.Tensor.sgn(input_tensor)
print('Output tensor: \n{}\n'.format(output_tensor))