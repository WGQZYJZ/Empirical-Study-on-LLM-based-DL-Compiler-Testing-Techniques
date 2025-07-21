'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_diagonal_\ntorch.Tensor.fill_diagonal_(_input_tensor, fill_value, wrap=False)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('Input: \n', _input_tensor)
torch.Tensor.fill_diagonal_(_input_tensor, fill_value=1, wrap=False)
print('Output: \n', _input_tensor)