'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.copy_\ntorch.Tensor.copy_(_input_tensor, src, non_blocking=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = torch.Tensor.copy_(_input_tensor, src=torch.randn(2, 3))
print('Output tensor: {}'.format(_output_tensor))