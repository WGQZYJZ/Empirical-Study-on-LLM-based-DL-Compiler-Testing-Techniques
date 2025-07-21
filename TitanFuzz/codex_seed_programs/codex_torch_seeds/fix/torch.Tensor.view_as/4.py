'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view_as\ntorch.Tensor.view_as(_input_tensor, other)\n'
import torch
_input_tensor = torch.rand(4, 3)
_output_tensor = _input_tensor.view_as(torch.rand(3, 4))
print('_input_tensor:', _input_tensor)
print('_output_tensor:', _output_tensor)