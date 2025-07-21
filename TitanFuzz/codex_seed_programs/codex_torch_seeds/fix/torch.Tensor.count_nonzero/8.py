'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
import torch
_input_tensor = torch.randn(1, 3, 3, requires_grad=True)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)
print('Input tensor:')
print(_input_tensor)
print('Output tensor:')
print(_output_tensor)