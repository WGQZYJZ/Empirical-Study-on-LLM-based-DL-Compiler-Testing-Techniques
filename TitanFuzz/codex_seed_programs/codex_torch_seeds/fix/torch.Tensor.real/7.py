'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.real\ntorch.Tensor.real(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(10, dtype=torch.float32)
print('Input tensor: {}'.format(_input_tensor))
_real_tensor = torch.Tensor.real(_input_tensor)
print('Real tensor: {}'.format(_real_tensor))