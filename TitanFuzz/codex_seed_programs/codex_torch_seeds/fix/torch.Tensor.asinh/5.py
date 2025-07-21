'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.asinh\ntorch.Tensor.asinh(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('Input Tensor:')
print(_input_tensor)
print('Output Tensor:')
print(_input_tensor.asinh())