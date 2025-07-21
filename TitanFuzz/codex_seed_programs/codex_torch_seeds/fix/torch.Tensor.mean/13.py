'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.rand(3, 4)
print('_input_tensor:', _input_tensor)
_mean_value = _input_tensor.mean(dim=0)
print('_mean_value:', _mean_value)
_mean_value = _input_tensor.mean(dim=1)
print('_mean_value:', _mean_value)
_mean_value = _input_tensor.mean(dim=0, keepdim=True)
print('_mean_value:', _mean_value)