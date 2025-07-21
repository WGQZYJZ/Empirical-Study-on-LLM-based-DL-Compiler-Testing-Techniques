'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.greater_\ntorch.Tensor.greater_(_input_tensor, other)\n'
import torch
_input_tensor = torch.tensor([(- 1), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
_output_tensor = torch.Tensor.greater_(_input_tensor, 5)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)
'\nTask 4: Call the API torch.Tensor.gt_\ntorch.Tensor.gt_(self, other)\n'
_output_tensor = _input_tensor.gt_(5)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)