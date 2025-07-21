'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.map_\ntorch.Tensor.map_(_input_tensor, tensor, callable\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = torch.Tensor.map_(_input_tensor, (lambda x: (x * x)))
print('Output tensor: {}'.format(_output_tensor))