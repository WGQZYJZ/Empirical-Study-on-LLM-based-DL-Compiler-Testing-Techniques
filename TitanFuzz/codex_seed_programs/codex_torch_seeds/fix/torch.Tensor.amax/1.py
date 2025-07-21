'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amax\ntorch.Tensor.amax(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(4, 3)
print('Input tensor: ', _input_tensor)
_max_tensor = torch.Tensor.amax(_input_tensor, dim=None, keepdim=False)
print('Max tensor: ', _max_tensor)