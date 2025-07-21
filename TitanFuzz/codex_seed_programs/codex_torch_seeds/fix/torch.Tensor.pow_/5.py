'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input Tensor:', _input_tensor)
print('Result:', _input_tensor.pow_(2))