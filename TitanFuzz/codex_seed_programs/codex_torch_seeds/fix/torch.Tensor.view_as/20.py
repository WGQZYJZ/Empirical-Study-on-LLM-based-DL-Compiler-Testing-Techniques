'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view_as\ntorch.Tensor.view_as(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(2, 3)
_other = torch.randn(3, 2)
_output_tensor = torch.Tensor.view_as(_input_tensor, _other)
print(_output_tensor)