'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flatten\ntorch.Tensor.flatten(_input_tensor, start_dim=0, end_dim=-1)\n'
import torch
_input_tensor = torch.rand(2, 3, 4)
_flatten_tensor = _input_tensor.flatten()
print('Input Tensor: {}'.format(_input_tensor))
print('Flatten Tensor: {}'.format(_flatten_tensor))