'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.randn(4, 4)
print('Input Tensor: \n{}'.format(_input_tensor))
_mean_tensor = _input_tensor.mean(dim=1, keepdim=True)
print('Mean Tensor: \n{}'.format(_mean_tensor))
_mean_tensor = _input_tensor.mean(dim=1, keepdim=False)
print('Mean Tensor: \n{}'.format(_mean_tensor))