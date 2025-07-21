'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inverse\ntorch.Tensor.inverse(_input_tensor)\n'
import torch
import numpy as np
import torch
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
_output_tensor = torch.Tensor.inverse(_input_tensor)
print('input_tensor:', _input_tensor)
print('output_tensor:', _output_tensor)