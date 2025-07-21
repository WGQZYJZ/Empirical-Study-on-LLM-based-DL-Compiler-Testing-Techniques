'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_zeros\ntorch.Tensor.new_zeros(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
print('Input tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.new_zeros(_input_tensor, (2, 3))
print('Output tensor:')
print(_output_tensor)