'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
_input_tensor = torch.rand(10, 10)
_output_tensor = torch.Tensor.reciprocal(_input_tensor)
print('Input tensor: ')
print(_input_tensor)
print('Output tensor: ')
print(_output_tensor)