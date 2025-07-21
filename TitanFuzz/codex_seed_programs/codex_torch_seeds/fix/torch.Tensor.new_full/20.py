'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: ')
print(_input_tensor)
_size = (4, 5)
print('Size: ')
print(_size)
_fill_value = 1.0
print('Fill value: ')
print(_fill_value)
_output_tensor = torch.Tensor.new_full(_input_tensor, _size, _fill_value)
print('Output tensor: ')
print(_output_tensor)