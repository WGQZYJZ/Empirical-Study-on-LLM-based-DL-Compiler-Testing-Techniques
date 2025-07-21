'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil\ntorch.Tensor.ceil(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.randn(2, 3)
print('Input Tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.ceil(_input_tensor)
print('Output Tensor:')
print(_output_tensor)