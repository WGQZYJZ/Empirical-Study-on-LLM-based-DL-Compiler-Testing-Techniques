'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
import numpy as np
_input_tensor = torch.randn(2, 3)
print('Input tensor is: {}'.format(_input_tensor))
_output_tensor = torch.Tensor.cummax(_input_tensor, dim=1)
print('Output tensor is: {}'.format(_output_tensor))