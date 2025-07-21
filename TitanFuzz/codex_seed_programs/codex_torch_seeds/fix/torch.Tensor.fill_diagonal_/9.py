'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_diagonal_\ntorch.Tensor.fill_diagonal_(_input_tensor, fill_value, wrap=False)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor: \n', _input_tensor)
_input_tensor.fill_diagonal_(fill_value=1)
print('Output tensor: \n', _input_tensor)