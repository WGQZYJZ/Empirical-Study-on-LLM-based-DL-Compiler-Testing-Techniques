'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum\ntorch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.rand(2, 3)
_sum_tensor = _input_tensor.sum(dim=1, keepdim=True)
print('input tensor: {}'.format(_input_tensor))
print('sum tensor: {}'.format(_sum_tensor))