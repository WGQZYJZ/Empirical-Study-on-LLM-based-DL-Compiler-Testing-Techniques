'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round\ntorch.Tensor.round(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input data: ')
print(_input_tensor)
_output_tensor = _input_tensor.round()
print('Output data: ')
print(_output_tensor)