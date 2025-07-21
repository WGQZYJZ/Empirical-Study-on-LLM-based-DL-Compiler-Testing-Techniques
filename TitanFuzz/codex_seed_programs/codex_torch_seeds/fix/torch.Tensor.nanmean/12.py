'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmean\ntorch.Tensor.nanmean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_input_tensor[(0, 1, 1)] = float('nan')
_input_tensor[(0, 1, 2)] = float('nan')
_input_tensor[(1, 2, 1)] = float('nan')
print(_input_tensor)
_output_tensor = torch.Tensor.nanmean(_input_tensor, dim=1, keepdim=False)
print(_output_tensor)