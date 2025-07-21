'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inverse\ntorch.Tensor.inverse(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
_inverse_tensor = torch.Tensor.inverse(_input_tensor)
print('Input tensor: \n', _input_tensor)
print('Inverse of input tensor: \n', _inverse_tensor)