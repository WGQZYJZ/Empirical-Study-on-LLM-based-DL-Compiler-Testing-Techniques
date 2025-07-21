'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_empty\ntorch.Tensor.new_empty(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('input tensor: {}'.format(_input_tensor))
_output_tensor = torch.Tensor.new_empty(_input_tensor, (2, 3))
print('output tensor: {}'.format(_output_tensor))