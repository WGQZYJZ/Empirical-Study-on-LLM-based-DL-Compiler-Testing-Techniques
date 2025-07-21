'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.abs_\ntorch.Tensor.abs_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 3)
print('Input tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.abs_(_input_tensor)
print('Output tensor:')
print(_output_tensor)