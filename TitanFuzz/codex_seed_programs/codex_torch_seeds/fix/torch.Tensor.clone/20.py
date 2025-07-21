'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clone\ntorch.Tensor.clone(_input_tensor, *, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('_input_tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.clone()
print('_output_tensor: {}'.format(_output_tensor))