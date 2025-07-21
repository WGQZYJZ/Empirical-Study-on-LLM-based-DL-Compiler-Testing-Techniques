'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagflat\ntorch.Tensor.diagflat(_input_tensor, offset=0)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.diagflat(_input_tensor, offset=0)
print('Output tensor:')
print(_output_tensor)