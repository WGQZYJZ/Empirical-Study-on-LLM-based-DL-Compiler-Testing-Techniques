'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
_input_tensor = torch.rand(2, 3, 4)
_output_tensor = torch.Tensor.cummin(_input_tensor, dim=0)
print('Input tensor: {}'.format(_input_tensor))
print('Output tensor: {}'.format(_output_tensor))