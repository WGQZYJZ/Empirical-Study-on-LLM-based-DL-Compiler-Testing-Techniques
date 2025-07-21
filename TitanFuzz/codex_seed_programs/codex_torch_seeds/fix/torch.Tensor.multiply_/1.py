'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply_\ntorch.Tensor.multiply_(_input_tensor, value)\n'
import torch
_input_tensor = torch.rand(5, 3)
print('Input tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.multiply_(_input_tensor, 2)
print('Output tensor:')
print(_output_tensor)