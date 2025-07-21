'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum\ntorch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(4, 4)
print(_input_tensor)
_sum = _input_tensor.sum()
print(_sum)
_sum = _input_tensor.sum(dim=0)
print(_sum)
_sum = _input_tensor.sum(dim=1)
print(_sum)
_sum = _input_tensor.sum(dim=1, keepdim=True)
print(_sum)
_sum = _input_tensor.sum(dim=1, keepdim=True, dtype=torch.int)
print(_sum)