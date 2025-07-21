'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
import torch
_input_tensor = torch.rand(1, 2, 3, 4)
print('Input tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.ravel(_input_tensor)
print('Output tensor:')
print(_output_tensor)