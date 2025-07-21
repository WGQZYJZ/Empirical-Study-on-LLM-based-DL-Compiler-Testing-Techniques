'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log2\ntorch.Tensor.log2(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.randn(1, 2, 3, 4)
print('Input tensor:', _input_tensor)
_output_tensor = torch.Tensor.log2(_input_tensor)
print('Output tensor:', _output_tensor)