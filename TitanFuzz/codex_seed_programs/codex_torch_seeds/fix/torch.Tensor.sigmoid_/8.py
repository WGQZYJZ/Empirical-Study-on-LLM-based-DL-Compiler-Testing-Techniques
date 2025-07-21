'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sigmoid_\ntorch.Tensor.sigmoid_(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.randn(2, 3)
print('_input_tensor:', _input_tensor)
_output_tensor = torch.Tensor.sigmoid_(_input_tensor)
print('_output_tensor:', _output_tensor)