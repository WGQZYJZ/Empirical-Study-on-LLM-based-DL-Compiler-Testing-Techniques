'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view_as\ntorch.Tensor.view_as(_input_tensor, other)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = _input_tensor.view_as(torch.tensor([[1, 2], [3, 4], [5, 6]]))
print('Input tensor: {}'.format(_input_tensor))
print('Output tensor: {}'.format(output_tensor))