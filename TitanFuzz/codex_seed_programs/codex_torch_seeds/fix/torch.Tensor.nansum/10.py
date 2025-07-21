'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nansum\ntorch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_input_tensor[(0, 1, 2)] = float('nan')
_input_tensor[(1, 0, 0)] = float('nan')
_input_tensor[(1, 0, 1)] = float('nan')
print('Input Tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.nansum(_input_tensor, dim=1, keepdim=False, dtype=None)
print('Output Tensor:')
print(_output_tensor)