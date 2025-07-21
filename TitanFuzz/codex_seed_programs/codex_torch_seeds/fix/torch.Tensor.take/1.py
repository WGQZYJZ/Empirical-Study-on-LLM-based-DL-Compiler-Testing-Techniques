'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor:')
print(_input_tensor)
_indices = torch.tensor([0, 2])
_output_tensor = _input_tensor.take(_indices)
print('Output tensor:')
print(_output_tensor)
_output_tensor = _input_tensor.take(_indices, dim=1)
print('Output tensor:')
print(_output_tensor)