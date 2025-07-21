'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sort\ntorch.Tensor.sort(_input_tensor, dim=-1, descending=False)\n'
import torch
_input_tensor = torch.randn(3, 5)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = torch.Tensor.sort(_input_tensor, dim=(- 1), descending=False)
print('Output tensor: {}'.format(_output_tensor))