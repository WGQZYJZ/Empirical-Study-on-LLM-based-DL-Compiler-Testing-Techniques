'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn\ntorch.Tensor.sgn(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(3, 3)
print('Input Tensor:', input_tensor)
output_tensor = input_tensor.sgn()
print('Output Tensor:', output_tensor)