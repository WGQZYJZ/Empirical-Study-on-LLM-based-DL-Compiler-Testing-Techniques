'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.detach(_input_tensor)
print('Output tensor:')
print(_output_tensor)