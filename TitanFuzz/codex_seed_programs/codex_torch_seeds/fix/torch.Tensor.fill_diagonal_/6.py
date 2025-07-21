'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_diagonal_\ntorch.Tensor.fill_diagonal_(_input_tensor, fill_value, wrap=False)\n'
import torch
_input_tensor = torch.randint(low=0, high=10, size=(4, 4))
print('Input tensor: \n', _input_tensor)
_fill_value = 1
_input_tensor.fill_diagonal_(_fill_value)
print('Output tensor: \n', _input_tensor)
_input_tensor = torch.randint(low=0, high=10, size=(4, 4))
print('Input tensor: \n', _input_tensor)
_fill_value = 1
_input_tensor.fill_diagonal_(_fill_value, wrap=True)
print('Output tensor: \n', _input_tensor)