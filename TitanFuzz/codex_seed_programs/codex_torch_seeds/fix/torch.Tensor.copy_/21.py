'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.copy_\ntorch.Tensor.copy_(_input_tensor, src, non_blocking=False)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('_input_tensor:', _input_tensor)
_output_tensor = torch.Tensor.copy_(_input_tensor)
print('_output_tensor:', _output_tensor)
print('_input_tensor == _output_tensor:', (_input_tensor == _output_tensor))
print('_input_tensor is _output_tensor:', (_input_tensor is _output_tensor))