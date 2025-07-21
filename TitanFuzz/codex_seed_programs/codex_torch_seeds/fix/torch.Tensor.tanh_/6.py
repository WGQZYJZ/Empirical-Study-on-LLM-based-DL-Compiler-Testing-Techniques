'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tanh_\ntorch.Tensor.tanh_(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
_output_tensor = torch.Tensor.tanh_(_input_tensor)
print('Input Tensor:')
print(_input_tensor)
print('Output Tensor:')
print(_output_tensor)