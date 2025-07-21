'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmean\ntorch.Tensor.nanmean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Input tensor: \n', _input_tensor)
_output_tensor = torch.Tensor.nanmean(_input_tensor, dim=0, keepdim=False)
print('Output tensor: \n', _output_tensor)