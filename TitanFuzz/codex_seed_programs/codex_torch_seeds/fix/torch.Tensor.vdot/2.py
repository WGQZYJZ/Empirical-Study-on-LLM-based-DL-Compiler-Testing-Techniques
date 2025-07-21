'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vdot\ntorch.Tensor.vdot(_input_tensor, other)\n'
import torch
_input_tensor = torch.rand(2, 3)
other = torch.rand(3, 2)
_output_tensor = _input_tensor.vdot(other)
print('_input_tensor:', _input_tensor)
print('other:', other)
print('_output_tensor:', _output_tensor)