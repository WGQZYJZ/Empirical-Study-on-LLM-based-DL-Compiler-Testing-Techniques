'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num_\ntorch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
_input_tensor = torch.randn(2, 3)
_input_tensor[0][0] = float('nan')
_input_tensor[0][1] = float('inf')
_input_tensor[0][2] = float('-inf')
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = torch.Tensor.nan_to_num_(_input_tensor)
print('Output tensor: {}'.format(_output_tensor))