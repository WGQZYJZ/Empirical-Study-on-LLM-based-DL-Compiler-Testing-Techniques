'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky_inverse\ntorch.Tensor.cholesky_inverse(_input_tensor, upper=False)\n'
import torch
_input_tensor = torch.rand(size=(3, 3))
_output_tensor = torch.Tensor.cholesky_inverse(_input_tensor, upper=False)
print('Input tensor: {}'.format(_input_tensor))
print('Output tensor: {}'.format(_output_tensor))