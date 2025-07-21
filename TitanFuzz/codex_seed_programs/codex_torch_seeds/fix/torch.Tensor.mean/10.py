'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.randn(4, 3)
_mean_result = torch.Tensor.mean(_input_tensor, dim=None, keepdim=False, dtype=None)
print('Input Tensor: {}'.format(_input_tensor))
print('Mean Result: {}'.format(_mean_result))