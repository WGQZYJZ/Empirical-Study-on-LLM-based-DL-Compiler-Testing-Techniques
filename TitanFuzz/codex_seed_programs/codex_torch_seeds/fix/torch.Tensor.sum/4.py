'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum\ntorch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(3, 4)
print('Input tensor: ', _input_tensor)
_sum_result = _input_tensor.sum(dim=0, keepdim=True)
print('Sum result: ', _sum_result)
_sum_result = _input_tensor.sum(dim=1, keepdim=False)
print('Sum result: ', _sum_result)
_sum_result = _input_tensor.sum(dim=None, keepdim=False)
print('Sum result: ', _sum_result)
_sum_result = _input_tensor.sum(dim=0, keepdim=False)
print('Sum result: ', _sum_result)