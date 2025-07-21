'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(_input_tensor, value)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor is: \n', _input_tensor)
_output_tensor = torch.Tensor.mul_(_input_tensor, 10)
print('Output tensor is: \n', _output_tensor)