'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow_\ntorch.Tensor.pow_(_input_tensor, exponent)\n'
import torch
_input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
print('Input tensor:')
print(_input_tensor)
print('\nOutput tensor:')
print(_input_tensor.pow_(2))
print('\nInput tensor:')
print(_input_tensor)