'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('_input_tensor = ')
print(_input_tensor)
_output_tensor = _input_tensor.any(dim=0, keepdim=False)
print('_output_tensor = ')
print(_output_tensor)