'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amax\ntorch.Tensor.amax(_input_tensor, dim=None, keepdim=False)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.Tensor.amax')
_input_tensor = torch.randn(3, 3)
print('_input_tensor = ', _input_tensor)
print('torch.Tensor.amax(_input_tensor, dim=None, keepdim=False) = ', torch.Tensor.amax(_input_tensor, dim=None, keepdim=False))