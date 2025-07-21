'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amax\ntorch.Tensor.amax(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.amax(_input_tensor)
print('Output tensor:')
print(_output_tensor)
_output_tensor = torch.Tensor.amax(_input_tensor, dim=0)
print('Output tensor:')
print(_output_tensor)
_output_tensor = torch.Tensor.amax(_input_tensor, dim=1)
print('Output tensor:')
print(_output_tensor)
_output_tensor = torch.Tensor.amax(_input_tensor, dim=1, keepdim=True)
print