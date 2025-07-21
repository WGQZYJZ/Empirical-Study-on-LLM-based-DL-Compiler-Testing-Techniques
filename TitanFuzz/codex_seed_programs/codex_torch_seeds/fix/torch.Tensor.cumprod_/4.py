'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod_\ntorch.Tensor.cumprod_(_input_tensor, dim, dtype=None)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: ')
print(_input_tensor)
print('\n')
_output_tensor = torch.Tensor.cumprod_(_input_tensor, dim=1)
print('Output tensor: ')
print(_output_tensor)
print('\n')