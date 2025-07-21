'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view_as\ntorch.Tensor.view_as(_input_tensor, other)\n'
import torch
_input_tensor = torch.rand(size=(3, 4, 5))
_other_tensor = torch.rand(size=(4, 5, 3))
_output_tensor = _input_tensor.view_as(_other_tensor)
print(_output_tensor)